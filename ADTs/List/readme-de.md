# Die lineare Datenstruktur Liste

#### Die verkettete Liste ist eine dynamische Datenstruktur, die die geordenete Speicherung von Datenelementen unterstützt. Die Anzahl der Objekte muss nicht im Voraus bekannt sein und bleibt für die Lebensdauer der Liste offen.

## Definition: Liste

##### Eine Liste ist eine endliche Folge von Elementen deren Länge (im Gegensatz zu einem Array) durch Hinzufügen und Subtrahieren von Elementen geändert werden kann.

Die Liste besteht aus Knoten wobei jeder Knoten (Node) aus zwei Teilen besteht:

- Knoteninhalt: Das eigentliche Listenelement was den Inhalt verwaltet
- Referenz: Dient der Verkettung der Liste und zeigt auf den nächsten Knoten in der Liste

Da der letzte Knoten per Definition keinen nächsten Knoten hat, muss der nicht referenzierte Nullwert dort stehen.

```python
class Node(): # Erstellt die Klasse für den Knoten
    def __init__(self, pContent):
        self.content = pContent # Hier wird der Knoteninhalt übergeben
        self.next = None # Dieses ist dann die Referenz zum nächsten Knoten
```
Dabei hat ein Listenelement keine Informationen über seine Position in der Liste. Er kennt nur die Adresse seines Nachfolgers.
###
![Darstellung einer Liste](https://perlgeek.de/images/dmisc/sll02.png)
####
Der Konstruktor der Liste definiert dann immer den Anfang der Liste (first), das Ende der Liste (last) welcher immer als Nachfolger NULL hat und den aktuellen (current) Knoten
```python
class List(): # Erstellt die Klasse für die Liste
    def __init__(self):
        self.first = None # Zeiger für den Anfang der Liste
        self.last = None # Zeiger für das Ende der Liste
        self.current = None # Zeiger für den aktuellen Knoten
```

## Operationen mit Listen

###### Listen lassen sich flexibel auf- und abbauen wozu man die folgenden Operationen benutzen kann:

**Append:** Bei dieser Methode lässt sich ein Listenelemente erstellen und an die Liste anketten.
```python
def append(self, pContent) # Fügt einen Parameter für den Inhalt hinzu
```
**Remove:** Bei dieser Methode lässt sich der aktuelle (current) Knoten aus der Liste entfernen.
```python
def remove(self) # Wichtig ist das vorher bis zum gewünschtem Objekt durch iteriert wurde
```
**Insert:** Bei dieser Methode lässt sich ein Listenelement erstellen und vor dem aktuellen (current) Knoten in die Liste einfügen.
```python
def insert(self, pContent) #Fügt einen Paramter für den Inhalt hinzu. Auch hier wichtig vorher durch zu iterarieren zum gewünschtem Knoten
```
**Concat:** Bei dieser Methode lassen sich alle Listenelemente einer anderen Liste der aktuellen Liste anketten, wobei die Liste von der wir die Listenelemente anhängen dabei geleert wird.
```python
def concat(self, pList) #Fügt einen Parameter für die Liste hinzu die angehang werden soll
```
##
Wie die meisten [abstrakten Datentypen](#abstrakte-datentypen-adt) ist die lineare **ADT-Liste** ein zusammengesetzter Datentyp. Jedes seiner Objekte besteht aus einer endlichen Anzahl von Teilobjekten oder Elementen und ist **linear** angeordnet.

Für lineare Listen gilt Folgendes:
1. Es kann nur ein Listenelement geben, das keinen Vorgänger hat und als **Anfang** (first) der Listen bezeichnet wird. 
2. Es kann nur ein Listenelement geben, das keine Nachfolger hat und als **Ende** (last) der Liste bezeichnet wird.
3. Die restlichen Listeneinträge haben genau einen **Vorgänger** und genau einen **Nachgänger**

## Abstrakte Datentypen (ADT)

Wenn man einen abstrakten Datentypen definiert, muss man sich keine Gedanken über die "Struktur", "innere Organisation" oder "Implementierung" der Daten machen. Du gibst einfach die Operation (Methode) an, die der ADT ausführen soll. 

Die bekanntesten ADT's in der Informatik sind:
- ADT List (Liste)
- ADT Stack (Stapel)
- ADT Queue (Schlagnge)
- ADT Binary search tree (Binärer Suchbaum)

Für kompaktes Lernen der Informatik Bereiche des Abiturs (NRW) schaut [hier](https://www.jonahsimon.de/informatik/lineare-strukturen-sortierung) vorbei.

Stand: 2024
