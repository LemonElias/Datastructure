class Node():
    # Creating a class: Node
    def __init__(self, pContent): # Constructor of the class with a parameter for the content
        self.content = pContent # Content of the Node
        self.next = None # Pointer to the next Node

class List():
    # Creating a class: List
    def __init__(self): # Constructor of the class
        self.first = None # Pointer to the first Node 
        self.last = None # Pointer to the last Node 
        self.current = None # Pointer to the current Node (for iteration)

    # Method to check if the list is empty
    def isEmpty(self):
        return self.first == None # If the first Node is None
    
    # Method to check if the list has access
    def hasAccess(self):
        return self.current != None # If the current Node is not None we have access
    
    # Method to go to the next Node
    def next(self):
        if self.hasAccess(): 
                self.current = self.current.next # Set the current Node to the next Node

    # Method to go to the first Node
    def toFirst(self):
        if self.isEmpty() is False:
            self.current = self.first # Set the current Node to the first Node

    # Method to go to the last Node
    def toLast(self):
        if self.isEmpty() is False:
            self.current = self.last # Set the current Node to the last Node

    # Method to get the content of the current Node
    def getContent(self):
        if self.hasAccess():
            return self.current.content # Return the content of the current Node which is set with the parameter pContent 
        else:
            return None
    
    # Method to set the content of the current Node
    def setContent(self, pContent):
        if self.hasAccess():
            self.current.content = pContent # Set the content of the current Node with the parameter pContent

    # Method to append an element to the list
    def append(self, pContent): # Adding a parameter for the content
        newNode = Node(pContent) # Create a new Node with the content pContent
        if self.isEmpty(): # If the list is empty we can set the first and last Node to the new Node because its the only node in the list
            self.first = newNode 
            self.last = newNode
        else:
            self.last.next = newNode # Set the next Node of the last Node to the new Node
            self.last = newNode # Makes the new Node the last Node
    
    # Method to insert an element to the list
    def insert(self, pContent): # Adding a parameter for the content
        newNode = Node(pContent) # Create a new Node with the content pContent
        if self.isEmpty() or self.current == self.first: # If the list is empty or the current Node is the first Node we can set the new Node as the first Node
            newNode.next = self.first 
            self.first = newNode
        else:
            self.toFirst() # Set the current Node to the first Node
            while self.current.next != self.current: # Iterate through the list until the next Node is the current Node
                self.next()
            newNode.next = self.current.next # Set the next Node of the new Node to the next Node of the current Node
            self.current.next = newNode # Set the next Node of the current Node to the new Node

    # Method to concat two lists
    def concat(self, pList): # Adding a parameter for the list to concat
        if pList.isEmpty() is False: 
            pList.toFirst() # Set the current Node of the list we want to concat to the first Node
            while pList.hasAccess(): # Iterate through the list we want to concat until we have no access which means we are at the end of the list
                self.append(pList.getContent()) # Append the content of the current Node of pList to the other list
                pList.next()
    
    # Method to remove the current Node
    def remove(self):
        if self.hasAccess():
            if self.current == self.first: # If the current Node is the first Node we can set the first Node to the next Node
                self.first = self.first.next
                if self.first == None: # If the first Node is None we have no Nodes in the list and we can set the last Node to None
                    self.last = None
            else: # If the current Node is not the first Node we have to iterate through the list to find the previous Node
                self.toFirst()
                while self.current.next != self.current: # Iterate through the list until the next Node is the current Node
                    self.next()
                if self.current == self.last: # If the current Node is the last Node we can set the last Node to the current Node
                    self.last = self.current
                self.current.next = self.current.next.next # Set the next Node of the current Node to the next Node of the next Node to remove the current Node

    # Extra: Method to print the list (thats not in the original implementation of the list but it helps to test the list)
    def printList(self):
        if self.isEmpty():
            print("List is empty") # If the list is empty we print that the list is empty
        else:
            print("---------") # Print a line to separate the lists
            self.toFirst()
            while self.hasAccess(): # Iterate through the list until we have no access which means we are at the end of the list
                print(self.getContent()) # Print the content of the current Node
                self.next()
            print("---------")


# Creates a new list named test_list
test_list = List()

# Test of isEmpty method
print(test_list.isEmpty())  # Should print True

# Test of append method
test_list.append(1)
test_list.printList()  # Should print 1
print(test_list.isEmpty())  # Should print False

# Test of append method
test_list.append(2)
test_list.printList()  # Should print 1, 2

# Test of concat method
test_list2 = List()
test_list2.append(3)
test_list2.append(4)
test_list.concat(test_list2)
test_list.printList()  # Should print 1, 2, 3, 4

# Test of remove method
test_list.toFirst()
test_list.remove()
test_list.printList()  # Should print 2, 3, 4