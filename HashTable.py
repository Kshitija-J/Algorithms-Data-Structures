# Hash Table: 0
class HashTable:
    def __init__(self,size):
        self.size = 100
        self.table = [[] for _ in range(size)]
        self.height = 0
    
    def _hash(self, key):
        return hash(key) % self.size
    
    def insert(self, key):
        index = self._hash(key)
        cur_height = len(self.table[index])
        self.table[index].append(key)
        self.height = max(self.height, cur_height+1)
    
    def search(self, key):
        index = self._hash(key)
        return key in self.table[index]
    
    def delete(self, key):
        index = self._hash(key)
        try:
            self.table[index].remove(key)
        except ValueError:
            raise Exception(f"Delete object {key} not found in the table")
    
    def print_table(self):
        for i in range(self.size):
            print(f"{i}: {self.table[i]}")

    
def hash1(input_op,size):
    hash1=HashTable(size)
    for operation, value in input_op:
        if operation == "0":
            try:
                hash1.delete(value)
                print(f"{value} deleted")
            except Exception as e:
                print(str(e))
        elif operation == "1":
            hash1.insert(value)
            print(f"{value} value inserted")
        elif operation == "2":
            if hash1.search(value):
                print(f"Value {value} found")
            else:
                print(f"Value {value} not found")
        else:
            print(f"Invalid operation: {operation}")

    print("Hash Table height:", hash1.height)
    hash1.print_table()