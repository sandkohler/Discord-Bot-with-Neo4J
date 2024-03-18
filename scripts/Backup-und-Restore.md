# Neo4j Backup und Restore

Neo4j bietet eingebaute Funktionen für das Backup und das Wiederherstellen von Datenbanken. Hier ist eine kurze Übersicht.

## Backup

Um ein Backup einer Neo4j-Datenbank zu erstellen, kannst du das neo4j-admin backup Kommando verwenden. Dieses Kommando erstellt ein vollständiges Backup der Datenbank.

```bash
neo4j-admin backup --backup-dir=/pfad/zum/backup --name=mein_backup
```

Ersetze /pfad/zum/backup mit dem Pfad, in dem das Backup gespeichert werden soll, und mein_backup mit dem Namen, welcher du für das Backup verwenden möchtest.

## Restore

Um eine Neo4j-Datenbank aus einem Backup wiederherzustellen, kannst du das neo4j-admin restore Kommando verwenden. Dieses Kommando stellt die Datenbank aus dem Backup wieder her.

```bash
neo4j-admin restore --from=/pfad/zum/backup/mein_backup --database=graph.db --force
```

Ersetze /pfad/zum/backup/mein_backup mit dem Pfad zum Backup, das du wiederherstellen möchtest, und graph.db mit dem Namen der Datenbank, die du wiederherstellen möchtest.

Bitte beachte, dass du Neo4j stoppen musst, bevor du eine Wiederherstellung durchführen kannst und dass die --force Option vorhandene Daten überschreibt.

## Automatisches Backup

Für Neo4j Aura (die Cloud-Version von Neo4j) werden automatische Backups erstellt. Du kannst die Einstellungen für automatische Backups in den Datenbankeinstellungen von Neo4j Aura anpassen.