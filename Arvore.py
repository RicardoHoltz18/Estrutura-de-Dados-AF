from Node import Node as TreeNode
from ListaSE import ListaSE

class CategoriaNode(TreeNode):
    def __init__(self, value):
        super().__init__(value)
        self.produtos = ListaSE()

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = CategoriaNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = CategoriaNode(value)
            else:
                self._insert_recursive(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = CategoriaNode(value)
            else:
                self._insert_recursive(current_node.right, value)
        else:
            print("Categoria já existe na árvore!")

    def find(self, value):
        return self._find_recursive(self.root, value)

    def _find_recursive(self, current_node, value):
        if current_node is None:
            return None
        elif value == current_node.value:
            return current_node
        elif value < current_node.value:
            return self._find_recursive(current_node.left, value)
        else:
            return self._find_recursive(current_node.right, value)

    def inorder_traversal(self):
        return self._inorder_traversal_recursive(self.root)

    def _inorder_traversal_recursive(self, current_node):
        result = []
        if current_node:
            result = self._inorder_traversal_recursive(current_node.left)
            result.append(current_node.value)
            result += self._inorder_traversal_recursive(current_node.right)
        return result
