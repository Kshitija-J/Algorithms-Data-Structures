import random

class SkipNode:
    def __init__(self, key=None, value=None, max_level=0):
        self.key = key
        self.value = value
        self.next_nodes = [None] * max_level

class SkipList:
    def __init__(self, max_level=16, p=0.5):
        self.head = SkipNode(max_level=max_level)
        self.max_level = max_level
        self.p = p
        self.level = 0
    
    def _random_level(self):
        level = 0
        while random.random() < self.p and level < self.max_level - 1:
            level += 1
        return level
    
    def insert(self, key, value):
        update = [None] * self.max_level
        curr = self.head
        for i in reversed(range(self.level)):
            while curr.next_nodes[i] and curr.next_nodes[i].key < key:
                curr = curr.next_nodes[i]
            update[i] = curr
        curr = curr.next_nodes[0]
        if curr and curr.key == key:
            curr.value = value
        else:
            new_node_level = self._random_level()
            if new_node_level > self.level:
                for i in range(self.level, new_node_level):
                    update[i] = self.head
                self.level = new_node_level
            new_node = SkipNode(key, value, new_node_level)
            for i in range(new_node_level):
                new_node.next_nodes[i] = update[i].next_nodes[i]
                update[i].next_nodes[i] = new_node
    
    def search(self, key):
        curr = self.head
        for i in reversed(range(self.level)):
            while curr.next_nodes[i] and curr.next_nodes[i].key < key:
                curr = curr.next_nodes[i]
        curr = curr.next_nodes[0]
        if curr and curr.key == key:
            return curr.value
        else:
            return None
    
    def delete(self, key):
        update = [None] * self.max_level
        curr = self.head
        for i in reversed(range(self.level)):
            while curr.next_nodes[i] and curr.next_nodes[i].key < key:
                curr = curr.next_nodes[i]
            update[i] = curr
        curr = curr.next_nodes[0]
        if curr and curr.key == key:
            for i in range(self.level):
                if update[i].next_nodes[i] != curr:
                    break
                update[i].next_nodes[i] = curr.next_nodes[i]
            while self.level > 0 and self.head.next_nodes[self.level-1] is None:
                self.level -= 1
            return True
        else:
            return False
    
    def get_all(self):
        values = []
        curr = self.head
        while curr.next_nodes[0]:
            curr = curr.next_nodes[0]
            values.append(curr.value)
        return values

def SkipListOperations(input_op):
    skip_list = SkipList()
    for operation, value in input_op:
        if operation == "0":
            if skip_list.delete(value):
                print(f"{value} deleted from the list")
            else:
                print(f"{value} not found in the list")
        elif operation == "1":
            skip_list.insert(value, value)
            print(f"{value} inserted in the list")
        elif operation == "2":
            if skip_list.search(value) is not None:
                print(f"{value} found in the list")
            else:
                print(f"{value} not found in the list")
