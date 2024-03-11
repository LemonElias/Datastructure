# Die lineare Datenstruktur Queue

#### Die Queue ist ein abstrakter Datentyp der als Puffer für die Zwischenspeicherung von Objekten in einer bestimmten Reihenfolge verwendet wird. Queues sind spezielle Listen, in denen Elemente an einem Ende eingefügt und nur an einem anderen Ende entnommen werden. Die Warteschlange ist der deutsche Begriff. 

## FIFO-Verfahren

Das **FIFO-Verfahren** steht für First In First Out-Verfahren und bezeichnet in der Informatik eine bestimmte Reihenfolge, in der Daten, die am längsten warten, zuerst bearbeitet bzw. ausgelesen werden. Datenmengen die nach dem FIFO-Prinzip arbeiten werden im Bereich der Betriebssysteme auch Pipes genannt.
###
<div style="text-align:center"><img src="https://leanbase.de/autoimg/uploads/w3200/bf3tgsm2g5qb76qcw2qhcmex29rm24pd9e3p5xek.png"></div>

##
Der Gegensatz zum FIFO-Verfahren ist das **LIFO** (Last In First Out)-Verfahren, auf dem der ADT Stack beruht.

## Definition: Queue

Die Queue besteht aus Knoten wobei jeder Knoten(Node) aus zwei Teilen besteht:

- Knoteninhalt: Das eigentliche Element was den Inhalt verwaltet
- Referenz: Dient der Verkettung der Queue und zeigt auf den nächsten Knoten in der Queue

Da der letzte Knoten per Definition keinen nächsten Knoten hat, muss der nicht referenzierte Nullwert dort stehen.

```python
class Node(): # Erstellt die Klasse für den Knoten
    def __init__(self, pContent):
        self.content = pContent # Hier wird der Knoteninhalt übergeben
        self.next = None # Dieses ist dann die Referenz zum nächsten Knoten
```
###
![Darstellung einer Queue](https://i.stack.imgur.com/EuReW.png)
####
Der Konstruktor der Queue definiert dann immer den Kopf der Queue (head), den Schwanz der Queue (tail) und den aktuellen (current) Knoten
```python
class Queue(): # Erstellt die Klasse für die Queue
    def __init__(self): 
        self.head = None # Zeiger für den Kopf der Queue
        self.tail = None # Zeiger für das Ende der Queue
        self.current = None # Zeiger für den aktuellen Knoten
```

## Operationen mit Queues

##### Queues lassen sich flexibel auf- und abbauen wozu man die folgenden Operationen benutzen kann:

**Enqueue:** Bei dieser Methode lässt sich ein Element am Ende der Schlange einfügen.
```python
def enqueue(self, pContent) # Fügt einen Parameter für den Inhalt hinzu
```
**Dequeue:** Bei dieser Methode lässt sich das Element am Kopf der Schlange entnehmen.
```python
def dequeue(self)
```
**Front:** Bei dieser Methode wird das Element am Kopf der Schlange wiedergegeben ohne es zu entfernen. 
```python
def front(self)
```
**isEmpty:** Bei dieser Methode wird gecheckt ob die Schlange leer ist und gibt einen booleschen Wert.
```python
def isEmpty(self)
```
##
Wie die meisten [abstrakten Datentypen](#abstrakte-datentypen-adt) ist die lineare **ADT-Queue** ein zusammengesetzter Datentyp. Jedes seiner Objekte besteht aus einer endlichen Anzahl von Teilobjekten oder Elementen und ist **linear** angeordnet.

Für lineare Listen gilt Folgendes:
1. Es kann nur ein Element geben, das am **Kopf** der Schlange ist (head). Dieses wird immer zuerst abgerufen nach dem FIFO-Prinzip
2. Es kann nur ein Element geben, das keine Nachfolger hat und als **Schwanz** (tail) der Queue bezeichnet wird.
3. Die restlichen Elemente lassen sich nicht abrufen.

## Abstrakte Datentypen (ADT)

Wenn man einen abstrakten Datentypen definiert, muss man sich keine Gedanken über die "Struktur", "innere Organisation" oder "Implementierung" der Daten machen. Du gibst einfach die Operation (Methode) an, die der ADT ausführen soll. 

Die bekanntesten ADT's in der Informatik sind:
- ADT List (Liste)
- ADT Stack (Stapel)
- ADT Queue (Schlagnge)
- ADT Binary search tree (Binärer Suchbaum)

Für kompaktes Lernen der Informatik Bereiche des Abiturs (NRW) schaut [hier](https://www.jonahsimon.de/informatik/lineare-strukturen-sortierung) vorbei.

Stand: 2024