class Node:

    # var3 = None

    """
    Tree node: left child, right child and data
    """
    def __init__(self, l = None, r = None, d = None):
        """
        Node constructor 
        @param A node data object
        """
        self.left = l  # Left Node (object class Node)
        self.right = r # Right Node (object class Node)
        self.data = d  # Data (object of class Data)

class Data:
    """
    Tree data: Any object which is used as a tree node data
    """
    def __init__(self, val1, val2):
        """
        Data constructor
        @param A list of values assigned to object's attributes
        """
        self.a1 = val1 # key
        self.a2 = val2 # data value

d1 = Data(1, 2)
print(d1.a1, d1.a2)

# n1 = Node(d = d1)

# create tree add(Node n)

#www.stackoverflow.com/questions/2598437/how-to-implement-a-binary-tree