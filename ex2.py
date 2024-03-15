class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.balance = 0

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        self._insert(self.root, key)

    def _insert(self, node, key):
        pivot = None
        current = self.root
        stack = []
        while current is not None:
            if current.balance != 0:
                pivot = current
            stack.append(current)
            if key < current.key:
                current = current.left
            else:
                current = current.right

        if key < node.key:
            node.left = Node(key)
            node.balance -= 1
        else:
            node.right = Node(key)
            node.balance += 1

        # Update balances
        while stack:
            current = stack.pop()
            if current == pivot:
                break
            if key < current.key:
                current.balance -= 1
            else:
                current.balance += 1

        # Identify cases
        if pivot is None:
            print("Case #1: Pivot not detected")
        elif (pivot.balance == 2 and key > pivot.right.key) or (pivot.balance == -2 and key < pivot.left.key):
            print("Case #2: A pivot exists, and a node was added to the shorter subtree")
        else:
            print("Case 3 not supported")

    def inorder(self, node):
        if node is not None:
            self.inorder(node.left)
            print(node.key, end=' ')
            self.inorder(node.right)

# Test cases
bst = BST()
print("Test Case 1 (Case 1):")
bst.insert(10)
bst.insert(5)
bst.insert(15)

print("\nTest Case 2 (Case 2):")
bst = BST()
bst.insert(10)
bst.insert(15)
bst.insert(5)

print("\nTest Case 3 (Case 3):")
bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(2)

print("\nTest Case 4 (Case 1 again):")
bst = BST()
bst.insert(10)
bst.insert(20)
bst.insert(30)
