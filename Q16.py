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

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, current, key):
        if current is None:
            return current

        if key < current.key:
            current.left = self._remove(current.left, key)
        elif key > current.key:
            current.right = self._remove(current.right, key)
        else:
            if current.left is None and current.right is None:
                return None
            if current.left is None:
                return current.right
            if current.right is None:
                return current.left

            successor = self._min_value_node(current.right)
            current.key = successor.key
            current.right = self._remove(current.right, successor.key)

        return current

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, current, result):
        if current:
            self._inorder(current.left, result)
            result.append(current.key)
            self._inorder(current.right, result)

bst = BinarySearchTree()

codes = [45, 25, 65, 20, 30, 60, 70]
for code in codes:
    bst.insert(code)

print("Árvore inicial em ordem crescente:", bst.inorder())

bst.remove(20)
print("Após remover 20 (nó folha):", bst.inorder())

bst.remove(25)
print("Após remover 25 (nó com um filho):", bst.inorder())

bst.remove(45)
print("Após remover 45 (nó com dois filhos):", bst.inorder())
