# Node class for red-black tree
class Node:
    def __init__(self, value, color='red'):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return f"({self.value}, {self.color})"


# Red-Black Tree class
class RBT:
    def __init__(self):
        self.root = None
        self.size = 0
        self.height = 0

    def insert(self, value):
        if self.root is None:
            self.root = Node(value, color='black')
            self.size += 1
            self.height += 1
            return
        node = self.root
        parent = None
        while node is not None:
            parent = node
            if value < node.value:
                node = node.left
            else:
                node = node.right
        new_node = Node(value)
        new_node.parent = parent
        if value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node
        self._insert_fixup(new_node)
        self.size += 1
        if self.height < self._height(self.root):
            self.height = self._height(self.root)

    def rbt(input_op):
        tree = RBT()
        # start_time = time.time()
        for operation, value in input_op:
                if operation == 0:
                    tree.delete(value)
                elif operation == 1:
                    tree.insert(value)
                    print(f"{value} value inserted in tree")
                elif operation == 2:
                    if tree.search(value):
                        print(f"{value} found in the tree")
                    else:
                        print(f"{value} not found in the tree")
                # print(f"Height of the tree: {tree.height()}")
        # end_time = time.time()
        # print(f"Total time taken: {1000*(end_time - start_time):.2f} ms")
        # tree.display()
