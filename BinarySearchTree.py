class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(key, self.root)
    
    def _insert(self, key, node):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(key, node.left)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(key, node.right)

    def search(self, key):
        return self._search(key, self.root)
    
    # def _search(self, key, node):
    #     if node is None:
    #         return False
    #     elif node.val == key:
    #         return True
    #     # elif cmp(key, node.val) < 0:
    #     elif key < node.val if key != node.val else 0:
    #         return self._search(key, node.left)
    #     else:
    #         return self._search(key, node.right)

    # def _search(self, key, node):
    #     if node is None:
    #         return False
    #     elif node.val == key:
    #         return True
    #     elif key < node.val if key != node.val else False:
    #         return self._search(key, node.left)
    #     else:
    #         return self._search(key, node.right)
    def _search(self, key, node):
        if node is None:
            return False
        elif node.val == key:
            return True
        elif key < node.val:
            return self._search(key, node.left)
        else:
            return self._search(key, node.right)



    
    def delete(self, key):
        self.root = self._delete(key, self.root)
    
    def _delete(self, key, node):
        if node is None:
            raise Exception(f"Delete object {key} not found in the tree")
        elif cmp(key, node.val) < 0:
            node.left = self._delete(key, node.left)
        elif cmp(key, node.val) > 0:
            node.right = self._delete(key, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_node = self._find_min(node.right)
                node.val = min_node.val
                node.right = self._delete(min_node.val, node.right)
        
        return node
    
    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node
    
    def height(self):
        return self._height(self.root)
    
    def _height(self, node):
        if node is None:
            return 0
        else:
            left_height = self._height(node.left)
            right_height = self._height(node.right)
            return 1 + max(left_height, right_height)
    
    def inorder_traversal(self):
        self._inorder_traversal(self.root)
        
    def _inorder_traversal(self, node):
        if node!=None:
            self._inorder_traversal(node.left)
            print(node.val)
            self._inorder_traversal(node.right)


def BST(input_op):
    bst = BinarySearchTree()
    for operation, value in input_op:
        if operation == "0":
            try:
                bst.delete(value)
                print(f"{value} deleted from tree")
            except Exception as e:
                print(str(e))
        elif operation == "1":
            bst.insert(value)
            print(f"{value} value inserted in tree")
        elif operation == "2":
            if bst.search(value):
                print(f"Value {value} found in tree")
            else:
                print(f"Value {value} not found in tree")
        else:
            print(f"Invalid operation: {operation}")

    # Print height
    print(f"Height of the tree after operation {operation}: {bst.height()}")
    print("Inorder traversal:")
    bst.inorder_traversal()

