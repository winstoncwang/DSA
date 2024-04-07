class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        # create a empty tree instead
        self.root = None
    
    def insert(self,value):
        new_node = Node(value)
        # cant use tmp=self.root here. Python variables are references to objects in memory, not the objects themselves.
        # if we use tmp=self.root, tmp = new_node. we are not changing self.root
        # tmp -> self.root, tmp -> new_node. 
        # does not mean self.root -> new_node
        if self.root is None:   
            self.root = new_node
            return True
        tmp = self.root
        while (True):
            if new_node.value == tmp.value:
                return False
            if new_node.value < tmp.value:
                if tmp.left is None:
                    tmp.left = new_node
                    return True
                tmp = tmp.left
            else:
                if tmp.right is None:
                    tmp.right = new_node
                    return True
                tmp = tmp.right

my_tree = BinarySearchTree()
my_tree.insert(50)
my_tree.insert(22)
my_tree.insert(55)
my_tree.insert(23)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
print(my_tree.root.left.right.value)