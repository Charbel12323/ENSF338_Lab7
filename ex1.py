import random
import time
import matplotlib.pyplot as plt

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.balance = 0

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.key:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if node is None:
            return False
        if node.key == key:
            return True
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)

    def measure_balance(self):
        self._measure_balance_recursive(self.root)

    def _measure_balance_recursive(self, node):
        if node is None:
            return -1
        left_height = self._measure_balance_recursive(node.left)
        right_height = self._measure_balance_recursive(node.right)
        node.balance = abs(left_height - right_height)
        return max(left_height, right_height) + 1

def generate_random_tasks():
    tasks = []
    integers = list(range(1, 1001))
    for _ in range(1000):
        random.shuffle(integers)
        tasks.append(integers.copy())
    return tasks

def measure_performance(tree, task):
    start_time = time.time()
    for num in task:
        tree.search(num)
    end_time = time.time()
    return end_time - start_time

def main():
    bst = BinarySearchTree()
    tasks = generate_random_tasks()
    balance_values = []
    search_times = []

    for task in tasks:
        for num in task:
            bst.insert(num)
        bst.measure_balance()
        max_balance = bst.root.balance
        balance_values.append(max_balance)
        search_time = measure_performance(bst, list(range(1, 1001)))
        search_times.append(search_time)

    plt.scatter(balance_values, search_times)
    plt.xlabel('Absolute Balance')
    plt.ylabel('Search Time (s)')
    plt.title('Balance vs. Search Time')
    plt.show()

if __name__ == "__main__":
    main()
