class BinaryTree:

    class TreeNode:
        # Create class: TreeNode
        def __init__(self, pContent):
            self.content = pContent # Set content to pContent
            self.left = BinaryTree() # Initialize left child of the node as a new BinaryTree instance. This represents the left subtree of the current node.
            self.right = BinaryTree() # Initialize right child of the node as a new BinaryTree instance. This represents the right subtree of the current node.

    # Create class: BinaryTree
    def __init__(self, pContent=None, pLeftTree=None, pRightTree=None): # If a content is provided, initialize a TreeNode with the given content. This node becomes the root of the BinaryTree.
        if pContent is not None:
            self.root = self.TreeNode(pContent) # Create a new TreeNode with the given content
            if pLeftTree is not None: # If a left subtree is provided, set the left child of the root node to the given left subtree
                self.root.left = pLeftTree 
            else:
                self.root.left = BinaryTree() # If no left subtree is provided, initialize the left child of the root node as a new BinaryTree instance
            if pRightTree is not None: # If a right subtree is provided, set the right child of the root node to the given right subtree
                self.root.right = pRightTree
            else:
                self.root.right = BinaryTree() # If no right subtree is provided, initialize the right child of the root node as a new BinaryTree instance
        else:
            self.root = None # If no content is provided, set the root node to None
    
    def isEmpty(self): # Check if the BinaryTree is empty
        return self.root is None
    
    def setContent(self, pContent):
        if pContent is not None:
            if self.isEmpty(): # If the BinaryTree is empty, create a new TreeNode with the given content and initialize the left and right children as new BinaryTree instances
                self.root = self.TreeNode(pContent)
                self.root.left = BinaryTree()
                self.root.right = BinaryTree()
            else:
                self.root.content = pContent # If the BinaryTree is not empty, set the content of the root node to the given content
    
    def getContent(self): # Get the content of the root node
        if self.isEmpty():
            return None
        else:
            return self.root.content
        
    def setLeftTree(self, pTree): # Set the left subtree of the root node
        if self.isEmpty() != True and pTree is not None:
            self.root.left = pTree

    def getLeftTree(self): # Get the left subtree of the root node
        if self.isEmpty():
            return None
        else:
            return self.root.left
    
    def setRightTree(self, pTree): # Set the right subtree of the root node
        if self.isEmpty() != True and pTree is not None:
            self.root.right = pTree

    def getRightTree(self): # Get the right subtree of the root node
        if self.isEmpty():
            return None
        else:
            return self.root.right

    # Extra: Method to print the tree (thats not in the original implementation of the tree but it helps to test the tree)    
    def printTree(self, indent=0):
        if self.isEmpty() != True:
            print("------") # Print "------" to separate the different nodes
            print(' ' * indent, self.root.content) # Print the content of the root node with the given indentation
            self.root.left.printTree(indent + 2) # Print the left subtree with an increased indentation
            self.root.right.printTree(indent + 2) # Print the right subtree with an increased indentation
            print("------") 
        else:
            print("Tree is empty") # If the tree is empty, print "Tree is empty"
        
# Creates a new BinaryTree named test_binarytree with the content "root"        
test_binarytree = BinaryTree("root")

# Test of the isEmpty method
print(test_binarytree.isEmpty()) # Should print False

# Test of the getContent method
print(test_binarytree.getContent()) # Should print root

# Test of the setLeftTree method
test_binarytree.setLeftTree(BinaryTree("left"))

# Test of the setRightTree method
test_binarytree.setRightTree(BinaryTree("right"))

# Test of the getLeftTree method
print(test_binarytree.getLeftTree().getContent()) # Should print left

# Test of the getRightTree method
print(test_binarytree.getRightTree().getContent()) # Should print right

# Test of the printTree method
test_binarytree.printTree() # Should print the tree with the root node "root" and the left and right subtrees "left" and "right"

