class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root

    def search(self, root, key):
        if root is None or root.val == key:
            return root
        if root.val < key:
            return self.search(root.right, key)
        return self.search(root.left, key)

    # Helper method to calculate the height of a node
    def height(self, node):
        if node is None:
            return 0
        else:
            return max(self.height(node.left), self.height(node.right)) + 1

    # Method to calculate the balance factor of each node
    def get_balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    # Utility function to print balance factor of each node
    def print_balance_factors(self, node):
        if node is not None:
            self.print_balance_factors(node.left)
            print(f"Node {node.val} balance factor: {self.get_balance(node)}")
            self.print_balance_factors(node.right)

# Example usage
bst = BST()
root = None
keys = [20, 10, 30, 5, 15, 25, 35]

# Inserting nodes
for key in keys:
    root = bst.insert(root, key)

# Searching for a node
search_key = 15
found_node = bst.search(root, search_key)
if found_node:
    print(f"Node found with key: {found_node.val}")
else:
    print("Node not found")

# Printing balance factors
bst.print_balance_factors(root)

