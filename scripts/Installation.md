# Neo4j Aura Installation

Neo4j Aura ist eine vollständig verwaltete Neo4j-Graphdatenbank, die in der Cloud gehostet wird. Hier sind die Schritte, um eine Neo4j Aura-Datenbank zu erstellen und darauf zuzugreifen.  

## Erstellen einer Neo4j Aura-Datenbank

1. Besuche die Neo4j Aura-Website.
2. Klicke auf "Get started for free" und erstelle ein Konto, wenn du noch keines hast.
3. Nachdem du dich angemeldet hast, klicke auf "Create a database".
4. Wähle den gewünschten Plan und die Region aus und klicke auf "Create Database".
5. Warte bis die Datenbank bereit ist. Dies kann einige Minuten dauern.

## Zugriff auf die Neo4j Aura-Datenbank

Nachdem die Datenbank erstellt wurde, kannst du darauf zugreifen und sie verwenden.  

1. Klicke auf "Open with Neo4j Browser", um die Datenbank im Webbrowser zu öffnen.
2. Du kannst auch auf die Datenbank über eine Anwendung zugreifen. Dazu benötigst du die Verbindungsinformationen, welche auf der Seite der Datenbank zu finden sind. Diese Informationen beinhalten die URI und das Passwort.

Hier ist ein Beispiel, wie du auf die Neo4j Aura-Datenbank zugreifen kannst:

```python
from neo4j import GraphDatabase

driver = GraphDatabase.driver("neo4j+s://6bf28e5e.databases.neo4j.io",
                              auth=("neo4j", "em9CZtLJX9l_xEtAX4m0mH5qg9h8lkzwpQuOwBq2Hig"))
```