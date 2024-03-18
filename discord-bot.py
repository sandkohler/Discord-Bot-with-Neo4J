import discord
import requests
from discord.ext import commands
from neo4j import GraphDatabase

driver = GraphDatabase.driver("neo4j+s://6bf28e5e.databases.neo4j.io",
                              auth=("neo4j", "em9CZtLJX9l_xEtAX4m0mH5qg9h8lkzwpQuOwBq2Hig"))

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


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


@bot.command()
async def befehlliste(ctx):
    await ctx.send("Liste der Befehle:\n !echo\n !generateimage\n !images\n !imageswithdescription\n (oder probiere es mal mit Hallo!)")


@bot.command()
async def echo(ctx, txt):
    await ctx.send(txt)


@bot.event
async def on_member_join(member):
    await member.send("Willkommen auf dem Community Server!")


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


@bot.command()
async def images(ctx):
    with driver.session() as session:
        result = session.run("MATCH (i:Image) RETURN i.url AS url")
        for record in result:
            await ctx.send(record["url"])


@bot.command()
async def imageswithdescription(ctx):
    with driver.session() as session:
        result = session.run("""
            MATCH (d:Description)-[:CREATED]->(i:Image)
            RETURN d.description AS description, i.url AS url
        """)
        for record in result:
            await ctx.send(f"Description: {record['description']}\nURL: {record['url']}")


@bot.command()
async def imagesfrom(ctx, username):
    with driver.session() as session:
        result = session.run("""
            MATCH (u:User {name: $username})-[:SENT]->(:Description)-[:CREATED]->(i:Image)
            RETURN i.url AS url
        """, username=username)
        for record in result:
            await ctx.send(record["url"])


@bot.command()
async def updatedescription(ctx, image_url, new_description):
    username = ctx.author.name
    with driver.session() as session:
        session.run("""
            MATCH (u:User {name: $username})-[:SENT]->(d:Description)-[:CREATED]->(i:Image {url: $image_url})
            SET d.description = $new_description
        """, username=username, image_url=image_url, new_description=new_description)
    await ctx.send("Die Beschreibung wurde aktualisiert.")


bot.run("OTg5ODkzNDU3MTkzNjA3MjE4.GlAtJW.idiIWsyM0iXue08shed_FJOuyQNROHjDRDAdPY")
