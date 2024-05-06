# Die lineare Datenstruktur Stack

#### Der Stack oder auch "Stapelspeicher" genannt beschreibt eine Datenstruktur, bei der man zu jeder Zeit nur das oberste Element abrufen kann. Außerdem kann auch ein neues Objekt nur ganz oben abgelegt werden. Ein Stack ist im Grunde eine spezielle Form der linearen Liste. Allerdings kann man bei einem Stack nicht auf tiefer liegende Elemente zugreifen sofern man nicht alle Elemente darüber entfernt. 

## LIFO-Verfahren

Das **LIFO-Verfahren** steht für Last In First Out-Verfahren und bezeichnet in der Informatik eine bestimmte Reihenfolge, in der Daten, die zuletzt eingefügt wurden, zuerst auch wieder entnommen werden. 
###
<div style="text-align:center"><img src="https://www.12manage.com/images/picture_lifo.gif"></div>

##
Der Gegensatz zum LIFO-Verfahren ist das **FIFO** (First In First Out)-Verfahren, auf dem der ADT Queue beruht.

## Definition: Stack

Der Stack besteht aus Knoten wobei jeder Knoten(Node) aus zwei Teilen besteht:

- Knoteninhalt: Das eigentliche Element was den Inhalt verwaltet
- Referenz: Dient der Verkettung des Stacks und zeigt auf den nächsten Knoten in dem Stack

Da der letzte Knoten per Definition keinen nächsten Knoten hat, muss der nicht referenzierte Nullwert dort stehen.

## Operationen mit Stacks

##### Stacks haben drei Operationen die dabei zum Einsatz kommen:

**Push:** Diese Methode legt ein neues Element auf den Stapel.
```python
def push(self, pContent) # Fügt einen Parameter für den Inhalt hinzu
```
**Pop:** Diese Methode nimmt das oberste Element vom Stapel
```python
def pop(self)
```
**Peek:** Dieses Methode gibt das oberste Element vom Stapel aus ohne es zu entfernen
```python
def peek(self)
```
**isEmpty:** Bei dieser Methode wird gecheckt ob die Schlange leer ist und gibt einen booleschen Wert zurück
```python
def isEmpty(self)
```
##
Wie die meisten [abstrakten Datentypen](#abstrakte-datentypen-adt) ist der lineare **ADT-Stack** ein zusammengesetzter Datentyp. Jedes seiner Objekte besteht aus einer endlichen Anzahl von Teilobjekten oder Elementen und ist **linear** angeordnet.

Für lineare Listen gilt Folgendes:
1. Es kann nur ein Element geben, das an der Obersten Position im Stack ist (top). Dieses wird immer zuerst abgerufen nach dem LIFO-Prinzip
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
