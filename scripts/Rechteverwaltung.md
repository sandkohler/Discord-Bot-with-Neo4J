# Neo4j Rechteverwaltung

Neo4j bietet eine umfangreiche Rechteverwaltung, die es ermöglicht, Benutzer und Rollen zu erstellen und zu verwalten. Hier ist eine kurze Übersicht.  

## Benutzer erstellen

Du kannst einen neuen Benutzer in Neo4j mit dem folgenden Befehl erstellen:

```cypher
CALL dbms.security.createUser('username', 'password', false)
```

Ersetze 'username' und 'password' durch den gewünschten Benutzernamen und das Passwort. Das letzte Argument gibt an, ob das Passwort bei der ersten Anmeldung geändert werden muss (true) oder nicht (false).

## Rollen erstellen

Du kannst eine neue Rolle in Neo4j mit dem folgenden Befehl erstellen:

```cypher
CALL dbms.security.createRole('role')
```

Ersetze 'role' durch den gewünschten Rollennamen.

## Benutzer einer Rolle hinzufügen

Du kannst einen Benutzer zu einer Rolle in Neo4j mit dem folgenden Befehl hinzufügen:

```cypher   
CALL dbms.security.addRoleToUser('role', 'username')
```

Ersetze 'role' durch den Rollennamen und 'username' durch den Benutzernamen.

## Rollen und Berechtigungen

Neo4j hat vier vordefinierte Rollen: 'admin', 'architect', 'publisher', 'editor' und 'reader'. Jede Rolle hat unterschiedliche Berechtigungen:  

- admin: Hat Zugriff auf alle Funktionen und Daten.
- architect: Kann das Schema ändern, hat aber keinen Zugriff auf Benutzer- und Rollenverwaltung.
- publisher: Kann Daten lesen, schreiben und das Schema ändern.
- editor: Kann Daten lesen und schreiben, kann aber das Schema nicht ändern.
- reader: Kann nur Daten lesen.

Du kannst auch benutzerdefinierte Rollen erstellen und ihnen spezifische Berechtigungen zuweisen.