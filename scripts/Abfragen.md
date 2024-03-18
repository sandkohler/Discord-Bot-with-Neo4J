# Neo4j Abfragen

Neo4j verwendet eine Abfragesprache namens Cypher, die speziell für die Interaktion mit Graphen entwickelt wurde. Hier ist eine kurze Übersicht über einige grundlegende Abfragen.  

## Knoten abfragen

Du kannst Knoten in Neo4j mit dem MATCH Befehl abfragen. Hier ist ein Beispiel, wie du alle User Knoten abfragen kannst:

```cypher
MATCH (u:User)
RETURN u
```

In diesem Beispiel werden alle User Knoten im Graphen zurückgegeben.

## Beziehungen abfragen

Du kannst auch Beziehungen zwischen Knoten abfragen. Hier ist ein Beispiel, wie du alle SENT Beziehungen abfragen kannst:

```cypher
MATCH (a:User)-[:SENT]->(b:User)
RETURN a, b
```

In diesem Beispiel werden alle Paare von User Knoten zurückgegeben, die durch eine SENT Beziehung verbunden sind.

## Filtern

Du kannst deine Abfragen mit dem WHERE Befehl filtern. Hier ist ein Beispiel, wie du alle User Knoten abfragen kannst, deren name Eigenschaft 'John' ist:

```cypher
MATCH (u:User)
WHERE u.name = 'John'
RETURN u
```

In diesem Beispiel werden alle User Knoten zurückgegeben, deren name Eigenschaft 'John' ist. 

## Aggregation

Du kannst auch Aggregationsfunktionen wie COUNT, AVG, MIN, MAX und SUM verwenden. Hier ist ein Beispiel, wie du die Anzahl der User Knoten abfragen kannst:

```cypher
MATCH (u:User)
RETURN COUNT(u)
```

In diesem Beispiel wird die Anzahl der User Knoten im Graphen zurückgegeben.