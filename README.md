# Discord Bot mit Neo4J

## Vorgehen

Wir haben im [Discord Developer Portal](https://discord.com/developers/docs/getting-started) einen Discord Bot erstellt, diesem haben wir einen Namen, sowie ein Profilbild und Berechtigungen gegeben. Danach mussten wir ihn nur noch in unseren Discord-Server einladen.

![Developer-Discord-Bot](./images/Developer-Discord-Bot.png)

Nachdem haben wir eine neue Instanz mit [Neo4J Aura](https://console.neo4j.io/) erstellt, damit wir unsere Neo4J Datenbank dort laufen lassen können.

![Neo4j-Aura-Instances](./images/Neo4j-Aura-Instances.png)

Nachdem haben wir mit dem [Python Script](discord-bot.py) begonnen, damit der Bot auch irgendwas machen kann und nicht nur in unserem Discord Server ist, sondern auch etwas machen kann. Dieses [Python Script](discord-bot.py) wird immer erweitert, falls noch neue Ideen dazukommen oder andere Anpassungen gemacht werden.

Damit der Bot auch läuft, wenn das [Python Script](discord-bot.py) Lokal nicht läuft, sondern einfach immer funktioniert hosten wir ihn gratis auf [Bot-Hosting.net](https://bot-hosting.net/?aff=720339805782671484).

## Datenbank Neo4J

Neo4J ist eine Graphdatenbank, die auf der Idee von Knoten und Kanten basiert. Wir haben uns für Neo4J entschieden, da es eine sehr gute Datenbank für Beziehungen ist und wir so mithilfe vom Discord Bot Beziehungen kreieren und später auch anzeigen können.

Um Neo4J in einem Python Script zu verwenden, kann einfach [Neo4J Python Driver](https://neo4j.com/developer/python/) installiert werden, mit diesem Befehl:

```bash
pip install neo4j
```

Un so kann Neo4J in einem Python Script verwendet werden:

```python
from neo4j import GraphDatabase 
``` 

Um überhaupt etwas in Neo4J zu speichern, muss zuerst eine Verbindung zur Datenbank hergestellt werden. Dies kann mit diesem Code gemacht werden:

```python
driver = GraphDatabase.driver("neo4j+s://6bf28e5e.databases.neo4j.io",
                              auth=("neo4j", "em9CZtLJX9l_xEtAX4m0mH5qg9h8lkzwpQuOwBq2Hig"))
``` 

Um die Verbindung mit der Datenbank zu nutzen, nutzen wir einen asynchronen Event Handler, der aufgerufen wird, wenn eine Nachricht im Discord-Server geschrieben wird, welche nicht vom Bot selbst stammt. Wenn die Nachricht "Hallo" beinhaltet reagiert der Bot mit diesem Emoji "👋". Aber egal, ob die Nachricht "Hallo" beinhaltet oder nicht wird die Nachricht in der Datenbank gespeichert.

```python
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    author = message.author.name
    content = message.content

    if "Hallo" in message.content:
        await message.add_reaction("👋")

    with driver.session() as session:
        session.run("""
            MERGE (a:User {name: $username})
            CREATE (m:Message {message: $message})
            CREATE (a)-[:SENT]->(m)
        """, username=author, message=content)

    await bot.process_commands(message)
``` 
Aber wie und was speichern wir in der Datenbank? Wir speichern den User und die Nachricht, welcher der User schreibt und stellen die Verbindung "Sent" her. Dies wird mit dem Befehl "MERGE" gemacht, welcher den User speicher, wenn er noch nicht existiert und mit dem Befehl "CREATE" wird die Nachricht gespeichert und die Verbindung "Sent" hergestellt.

Mit der generateimage Funktion können Bilder erstellt werden, wobei später über die Beziehungen in der Datenbank nachverfolgt werden kann welcher User, mit welcher Beschreibung, welches Bild erstellt hat. Um diese Funktion vom Bot auszuführen, muss im Discord-Server der Befehl "!generateimage" geschrieben werden.

```python
@bot.command()
async def generateimage(ctx):
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel

    await ctx.send("Gib den Prompt ein, um das Bild zu generieren:")
    msg = await bot.wait_for('message', check=check)
    description = msg.content

    url = "https://api.edenai.run/v2/image/generation"
    payload = {
        "response_as_dict": True,
        "attributes_as_list": False,
        "show_original_response": False,
        "resolution": "512x512",
        "num_images": 2,
        "providers": "replicate",
        "text": description
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiM2U1MjQ1ODgtZDI5ZS00ZDhiLTljZDItODRlMTRkOTEwMDFiIiwidHlwZSI6ImFwaV90b2tlbiJ9.872nbP_BksM4IV-dkFlL1TSmVjBCg2oIyvgmYbdjssI"
    }

    response = requests.post(url, json=payload, headers=headers)
    image_url = response.json()["replicate"]["items"][0]["image_resource_url"]

    with driver.session() as session:
        session.run("""
            MERGE (u:User {name: $username})
            CREATE (d:Description {description: $description})
            CREATE (i:Image {url: $image_url})
            CREATE (u)-[:SENT]->(d)
            CREATE (d)-[:CREATED]->(i)
        """, username=ctx.author.name, description=description, image_url=image_url)

    await ctx.send(image_url)
```

Um das Bild zu generieren, wird die API von [EdenAI](https://www.edenai.run/) verwendet. Mit dieser API kann ein Bild generiert werden, welches auf einer Beschreibung basiert. Die Beschreibung wird in der Datenbank gespeichert und mit dem Bild verknüpft.

In der Datenbank sehen die Beziehungen dann so aus, wie im Bild unten. Der Benutzer ist der grüne Kreis mit einer SENT Beziehung zu einem roten Kreis, der Beschreibung und die Beschreibung hat eine CREATED Beziehung zu einem blauen Kreis, also dem Bild.

![DatenbankGraph](/images/DatenbankGraph.png)

### Image Generation

Im Frontend, also in Discord selbst, sieht die Bildgenerierung dann so aus:

![generateImage](images/!generateImage.png)

So gebe ich zuerst den Command `!generateimage` ein, darauf antwortet der Bot mit der Nachricht "Gib den Prompt ein, um das Bild zu generieren:" 

Danach kann der Prompt eingegeben werden, welcher die Beschreibung des Bildes ist. Der Bot antwortet dann mit dem generierten Bild und speichert die Beschreibung und das Bild in der Datenbank.

![img.png](images/kircheAufEinemBergMitSonnenschein.png)

### Jokes

(Bitte alle Witze mit Humor nehmen 😉)

Ein weiteres Feature, welches wir hinzugefügt haben, sind Witze. Mit dem Command `!joke` wird von der API [JokeAPI](https://jokeapi.dev/) ein Witz generiert und im Discord-Chat angezeigt.

```python
@bot.command()
async def joke(ctx):
    url = "https://v2.jokeapi.dev/joke/Any?type=single"
    response = requests.get(url)
    joke = response.json()["joke"]
    joke_id = response.json()["id"]

    await ctx.send(joke)

    with driver.session() as session:
        session.run("""
            MERGE (j:Joke {id: $joke_id, joke: $joke})
        """, joke_id=joke_id, joke=joke)
```

Das funktioniert ganz einfach so:

![joke](images/joke.png)

Nun bekommt man einfach einen Witz zurück, diesen kann man Filtern.

Entweder nutzt man dazu den Command `!jokebycategory` oder `!jokewithblacklist`, hier je ein Beispiel:

![jokebycategory](images/jokebycategory.png)

![jokewithblacklist](images/jokewithblacklist.png)

In der Datenbank werden die Witze immer mit einer `BELONGS_TO` Beziehung zu einer Kategorie gespeichert.

![DatenbankGraphJoke](images/jokesbycategorygraph.png)

## Reflexion

Für mich war es das erste Python & Neo4j Projekt, also ich habe schon von Python gehört, aber noch nichts damit umgesetzt. Neo4j kannte ich bis zum NoSQL Modul nicht und musste ich wie Python auch neu lernen, dies hat mir aber sehr viel Spass gemacht, vor allem die verschiedene Commands auszuprobieren. Diese beiden Technologien mit Discord zu verbinden war eine gute Idee, da ich Discord oft privat nutze und mir es so Freude bereitet hat, als ich meinen eigenen Bot erstellte, den ich nutzen konnte. Insgesamt habe ich viel gelernt und bin ich sehr zufrieden mit dem Projekt.

(Falls dir dieses Projekt gefällt, schau dir doch dieses Projekt an: [Twitch-Bot-with-Neo4J](https://github.com/LinusTimoDaniels/Twitch-Bot-with-Neo4J))