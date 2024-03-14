class Node():
    # Creating a class: Node
    def __init__(self, pContent): # Constructor of the class with a parameter for the content
        self.content = pContent # Content of the Node
        self.next = None # Pointer to the next Node

class Stack():
    # Creating a class: Stack
    def __init__(self): # Constructor of the class
        self.top = None # Pointer to the first Node
        self.current = None # Pointer to the current Node (for iteration)

    # Method to check if the stack is empty
    def isEmpty(self):
        return self.top == None # If the first Node is None
    
    # Method to add an element to the stack
    def push(self, pContent): # Adding a parameter for the content
        if pContent is not None: 
            newNode = Node(pContent) # Create a new Node with the content pContent if the content is not None
            newNode.next = self.top # Set the next Node of the new Node to the current top Node
            self.top = newNode # Makes the new Node the top Node

    # Method to remove the first element from the stack
    def pop(self):
        if self.isEmpty() is False: 
            self.top = self.top.next # Set the top Node to the next Node
        else:
            return None
        
    # Method to get the content of the first Node
    def peek(self):
        if self.isEmpty() is False:
            return self.top.content # Return the content of the top Node
        else:
            return None
        
    # Method to print the stack (thats not in the original implementation of the stack but it helps to test the list)
    def printStack(self):
        print("----------------") # Print a line to separate the different stacks
        if self.isEmpty() is False:
            self.current = self.top
            while self.current is not None: # Iterate through the stack until the current Node is None
                print(self.current.content)
                self.current = self.current.next
            print("----------------")
        else:
            print("Stack is empty") # If the stack is empty we print "Stack is empty"



# Creates a new Stack named test_stack
test_stack = Stack()

# Test of isEmpty method
print(test_stack.isEmpty()) # Output: True

# Test of push method
test_stack.push(1)
print(test_stack.peek()) # Output: 1
print(test_stack.isEmpty()) # Output: False

# Test of push method
test_stack.push(2)
print(test_stack.peek()) # Output: 2

# Test of pop method
test_stack.pop()
print(test_stack.peek()) # Output: 1

# Test of pop method
test_stack.pop()
print(test_stack.isEmpty()) # Output: True

# Test printStack method
test_stack.printStack() # Output: Stack is empty