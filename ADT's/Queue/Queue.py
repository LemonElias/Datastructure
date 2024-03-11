class Node():
    # Creating a class: Node
    def __init__(self, pContent): # Constructor of the class with a parameter for the content
        self.content = pContent # Content of the Node
        self.next = None # Pointer to the next Node

class Queue():
    # Creating a class: Queue
    def __init__(self): # Constructor of the class
        self.head = None # Pointer to the first Node
        self.tail = None # Pointer to the last Node
        self.current = None # Pointer to the current Node (for iteration)
    
    # Method to check if the queue is empty
    def isEmpty(self):
        return self.head == None # If the first Node is None
    
    # Method to add an element to the queue
    def enqueue(self, pContent): # Adding a parameter for the content
        if pContent is not None: 
            newNode = Node(pContent) # Create a new Node with the content pContent if the content is not None
            if self.isEmpty(): # If the queue is empty we can set the first and last Node to the new Node because its the only node in the queue
                self.head = newNode
                self.tail = newNode
            else:
                self.tail.next = newNode # Set the next Node of the last Node to the new Node
                self.tail = newNode # Makes the new Node the last Node

    # Method to remove an element from the queue
    def dequeue(self):
        if self.isEmpty() is False: 
            self.head = self.head.next # Set the first Node to the next Node
        else:
            return None

    # Method to get the content of the first Node
    def front(self):
        if self.isEmpty() is False:
            return self.head.content # Return the content of the first Node
        else:
            return None
        
    # Method to print the queue (thats not in the original implementation of the queue but it helps to test the list)
    def printQueue(self):
        print("----------------") # Print a line to separate the different queues
        if self.isEmpty() is False:
            self.current = self.head
            while self.current is not None: # Iterate through the queue until the current Node is None
                print(self.current.content)
                self.current = self.current.next
            print("----------------")
        else:
            print("Queue is empty") # If the queue is empty we print "Queue is empty"



# Creates a new Queue named test_queue
test_queue = Queue()

# Test of isEmpty method
print(test_queue.isEmpty())  # Should print True

# Test of enqueue method
test_queue.enqueue(1)
print(test_queue.front())  # Should print 1
print(test_queue.isEmpty())  # Should print False

# Test of enqueue method
test_queue.enqueue(2)
print(test_queue.front())  # Should print 1 (since 1 is at the front of the queue)

# Test dequeue method
print(test_queue.dequeue())  # Should print None (since dequeue has no return)
print(test_queue.front())  # Should print 2

# Test dequeue method until queue is empty
test_queue.dequeue()
print(test_queue.isEmpty())  # Should print True

# Test printQueue method
test_queue.printQueue()  # Should print "Queue is empty"