class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.height(z.left), self.height(z.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))

        return y

    def _right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))

        return x

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)

        root.height = 1 + max(self.height(root.left), self.height(root.right))

        balance = self.get_balance(root)

        # Left Left Case
        if balance > 1 and key < root.left.key:
            return self._right_rotate(root)

        # Right Right Case
        if balance < -1 and key > root.right.key:
            return self._left_rotate(root)

        # Left Right Case
        if balance > 1 and key > root.left.key:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)

        # Right Left Case
        if balance < -1 and key < root.right.key:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        return root

    def get_balance(self, root):
        if not root:
            return 0
        return self.height(root.left) - self.height(root.right)

    def print_inorder(self, node):
        if node:
            self.print_inorder(node.left)
            print(node.key, end=" ")
            self.print_inorder(node.right)

    def test(self):
        print("Test cases:")
        # Case 3a: adding a node to an outside subtree
        print("\nCase 3a:")
        avl_tree = AVLTree()
        avl_tree.insert(30)
        avl_tree.insert(20)
        avl_tree.insert(40)
        avl_tree.insert(10)
        avl_tree.insert(25)
        avl_tree.insert(35)
        avl_tree.insert(50)
        avl_tree.insert(5)
        avl_tree.print_inorder(avl_tree.root)

        # Case 3b: Not supported
        print("\nCase 3b (Not supported):")
        avl_tree = AVLTree()
        avl_tree.insert(10)
        avl_tree.insert(20)
        avl_tree.insert(30)
        avl_tree.insert(5)
        avl_tree.insert(1)
        avl_tree.print_inorder(avl_tree.root)


# Test AVL Tree
avl = AVLTree()
avl.test()