class SplayNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return f"SplayNode({self.key})"


class SplayTree:
    def __init__(self):
        self.root = None

    def _rotate_left(self, node):
        parent = node.parent
        grandparent = parent.parent

        parent.right = node.left
        if node.left is not None:
            node.left.parent = parent

        node.left = parent
        parent.parent = node

        node.parent = grandparent
        if grandparent is not None:
            if grandparent.left == parent:
                grandparent.left = node
            else:
                grandparent.right = node
        else:
            self.root = node

    def _rotate_right(self, node):
        parent = node.parent
        grandparent = parent.parent

        parent.left = node.right
        if node.right is not None:
            node.right.parent = parent

        node.right = parent
        parent.parent = node

        node.parent = grandparent
        if grandparent is not None:
            if grandparent.left == parent:
                grandparent.left = node
            else:
                grandparent.right = node
        else:
            self.root = node

    def _splay(self, node):
        while node.parent is not None:
            parent = node.parent
            grandparent = parent.parent
            if grandparent is None:
                # Zig step
                if parent.left == node:
                    self._rotate_right(node)
                else:
                    self._rotate_left(node)
            else:
                if grandparent.left == parent:
                    if parent.left == node:
                        # Zig-Zig step
                        self._rotate_right(parent)
                        self._rotate_right(node)
                    else:
                        # Zig-Zag step
                        self._rotate_left(node)
                        self._rotate_right(node)
                else:
                    if parent.right == node:
                        # Zig-Zig step
                        self._rotate_left(parent)
                        self._rotate_left(node)
                    else:
                        # Zig-Zag step
                        self._rotate_right(node)
                        self._rotate_left(node)

    def insert(self, key):
        new_node = SplayNode(key)
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            parent = None
            while current_node is not None:
                parent = current_node
                if key < current_node.key:
                    current_node = current_node.left
                elif key > current_node.key:
                    current_node = current_node.right
                else:
                    return

            new_node.parent = parent
            if key < parent.key:
                parent.left = new_node
            else:
                parent.right = new_node

            self._splay(new_node)

    def search(self, key):
        current_node = self.root
        while current_node is not None:
            if key < current_node.key:
                current_node = current_node.left
            elif key > current_node.key:
                current_node = current_node.right
            else:
                self._splay(current_node)
                return current_node

        return None

    def delete(self, key):
        node = self.search(key)
        if node is None:
            return

        if node.left is None:
            # Case 1: Node has no left child
            new_root = node.right
        elif node.right is None:
            # Case 2: Node has no right child
            new_root =         node.left
        else:
            # Case 3: Node has both left and right children
            successor = node.right
            while successor.left is not None:
                successor = successor.left

            if successor.parent != node:
                successor.parent.left = successor.right
                if successor.right is not None:
                    successor.right.parent = successor.parent

                successor.right = node.right
                node.right.parent = successor

            successor.left = node.left
            node.left.parent = successor

            new_root = successor

        if node.parent is not None:
            if node.parent.left == node:
                node.parent.left = new_root
            else:
                node.parent.right = new_root
        else:
            self.root = new_root

        if new_root is not None:
            new_root.parent = node.parent

    def in_order_traversal(self):
        if self.root is not None:
            result = []
            self._in_order_traversal_helper(self.root, result)
            return result
        else:
            return []

    def _in_order_traversal_helper(self, node, result):
        if node.left is not None:
            self._in_order_traversal_helper(node.left, result)

        result.append(node.key)

        if node.right is not None:
            self._in_order_traversal_helper(node.right, result)


    

def Splay(input_op):
    splay_tree = SplayTree()
    for operation, value in input_op:
        if operation == "0":
            try:
                splay_tree.delete(value)
                print(f"{value} deleted from tree")
            except Exception as e:
                print(str(e))
        elif operation == "1":
            splay_tree.insert(value)
            print(f"{value} value inserted in tree")
        elif operation == "2":
            if splay_tree.search(value):
                print(f"Value {value} found in tree")
            else:
                print(f"Value {value} not found in tree")
        else:
            print(f"Invalid operation: {operation}")
        
        # Print height
        print(f"Height of the tree after operation {operation}: {get_height(splay_tree.root)}")

    # Print in-order traversal
    print("In-order traversal:")
    for value in splay_tree.in_order_traversal():
        print(value)



def get_height(node):
    if node is None:
        return 0
    else:
        return max(get_height(node.left), get_height(node.right)) + 1
