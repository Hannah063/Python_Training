class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_recursion(self.root, value)

    def insert_recursion(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self.insert_recursion(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self.insert_recursion(current_node.right, value)

    def search(self, value):
        result = self.search_recursion(self.root, value)
        if result:
            print("Node is existing")
        else:
            print("Node is not existing")
    
    def search_recursion(self, current_node, value):
        if current_node is None:
            return False
        
        if current_node.value == value:
            return True
        
        if current_node.value < value:
            self.search_recursion(current_node.left, value)
        else:
            self.search_recursion(current_node.right, value)

bst = BinarySearchTree()

#45, 12, 68, 23, 7
bst.insert(45)
bst.insert(12)
bst.insert(68)
bst.insert(23)
bst.insert(7)

bst.search(7)
bst.search(38)