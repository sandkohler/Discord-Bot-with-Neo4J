# Neo4j Skalierung

Neo4j bietet verschiedene Möglichkeiten zur Skalierung, um die Leistung zu verbessern und größere Datenmengen zu verarbeiten. Hier ist eine kurze Übersicht.  

## Horizontale Skalierung

Neo4j unterstützt horizontale Skalierung durch seine Cluster-Architektur. In einem Neo4j-Cluster können mehrere Instanzen von Neo4j gleichzeitig laufen und die Last teilen. Dies wird oft als "Skalierung nach außen" bezeichnet. Ein Neo4j-Cluster besteht aus mehreren Arten von Knoten:  

- **Leader**: Dieser Knoten ist für das Schreiben von Daten verantwortlich.
- **Follower**: Diese Knoten replizieren die Daten des Leaders und können Leseanfragen bedienen.
- **Read Replicas**: Diese Knoten replizieren die Daten und sind ausschließlich für Leseanfragen vorgesehen.

## Vertikale Skalierung

Vertikale Skalierung, auch bekannt als "Skalierung nach oben", bezieht sich auf das Hinzufügen von mehr Ressourcen (wie CPU, RAM oder Speicher) zu einer einzelnen Neo4j-Instanz, um die Leistung zu verbessern.  

## Neo4j Aura

Neo4j Aura, die Cloud-Version von Neo4j, bietet automatische Skalierung. Du kannst die Größe deiner Datenbank jederzeit ändern, um mehr Speicherplatz oder Rechenleistung hinzuzufügen. Neo4j Aura passt auch automatisch die Anzahl der Read Replicas an, um die Leseleistung zu optimieren.  

## Caching

Neo4j verwendet ein ausgeklügeltes Caching-System, um die Leistung zu verbessern. Es hält häufig verwendete Daten im Speicher, um schnellen Zugriff zu ermöglichen. Du kannst die Cachegröße in den Neo4j-Konfigurationseinstellungen anpassen.