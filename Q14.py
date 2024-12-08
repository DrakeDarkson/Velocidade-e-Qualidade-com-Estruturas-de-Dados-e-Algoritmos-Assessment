class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current, key):
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert(current.left, key)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert(current.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, current, key):
        if current is None:
            return False
        if current.key == key:
            return True
        elif key < current.key:
            return self._search(current.left, key)
        else:
            return self._search(current.right, key)

bst = BinarySearchTree()

prices = [100, 50, 150, 30, 70, 130, 170]
for price in prices:
    bst.insert(price)

price_to_find = 70
if bst.search(price_to_find):
    print(f"Price {price_to_find} is available.")
else:
    print(f"Price {price_to_find} is not available.")
