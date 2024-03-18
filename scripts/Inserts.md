# Neo4j Inserts

In Neo4j, Daten einzufügen bedeutet, Knoten und Beziehungen im Graphen zu erstellen. Hier ist eine kurze Übersicht, wie du das tun kannst.  

## Knoten erstellen

Einen Knoten in Neo4j repräsentiert eine Entität oder ein Objekt. Du kannst einen Knoten mit dem CREATE Befehl erstellen. Hier ist ein Beispiel, wie du einen User Knoten erstellen kannst:

```cypher
CREATE (u:User {name: 'username'})
```

In diesem Beispiel wird ein User Knoten mit der Eigenschaft name erstellt, die den Wert 'username' hat.

## Beziehungen erstellen

Beziehungen in Neo4j verbinden Knoten und repräsentieren die Interaktionen zwischen ihnen. Du kannst eine Beziehung mit dem CREATE Befehl erstellen. Hier ist ein Beispiel, wie du eine SENT Beziehung zwischen zwei User Knoten erstellen kannst:

```cypher
MATCH (a:User {name: 'Alice'}), (b:User {name: 'Bob'})
CREATE (a)-[:SENT]->(b)
```

In diesem Beispiel wird eine SENT Beziehung von einem User Knoten namens 'Alice' zu einem User Knoten namens 'Bob' erstellt.

## Daten einfügen

Du kannst auch Daten aus einer CSV-Datei in Neo4j einfügen oder einfach mit Cypher Befehlen. Hier ist ein Beispiel, wie du einen Message Knoten erstellen und eine SENT Beziehung von einem User Knoten zu diesem Message Knoten erstellen kannst:

```cypher
MATCH (u:User {name: 'Alice'})
CREATE (m:Message {content: 'Hello, Neo4j!'})
CREATE (u)-[:SENT]->(m)
```

In diesem Beispiel wird ein Message Knoten mit einer Eigenschaft content erstellt, die den Wert 'Hello, Neo4j!' hat. Dann wird eine SENT Beziehung von einem User Knoten namens 'Alice' zu diesem Message Knoten erstellt.
