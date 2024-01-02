import sys
import time
import random
import BinarySearchTree as bst
import HashTable as hash1
import RedBlackTree as tree
import SplayTree as splay_tree
import SkipList as skip_list

input_op = [] 

def reading_input(inputfile):
    with open(inputfile, 'r') as file:
        start_time = time.time() # start measuring time
        for line in file:
            # print(line)
            # line = line.strip()
            fields = line.split()
            if len(fields) != 2:
                 print("Error: Input doesn't contain 2 fields.")
            else:
                operation, value = fields
            input_op.append((operation,int(value)))
            print("value",value)
        # print(input_op, type(operation))
        return input_op

#Main
if __name__ == "__main__":

    n = len(sys.argv)

    if n != 3:
        print("Invalid command entry. Enter in this format: ")
        print("python3 algo.py <IntegerValue> <inputfile Name>")
    else:
        ds_value = sys.argv[1]
        inputfile = sys.argv[2]

        print("input file", inputfile)
        print("Data structure: ", ds_value)

    if ds_value == '0':
        print("Hash Table")
        start_time = time.time()
        input_op = reading_input(inputfile)
        size=100
        hash1.hash1(input_op, size)
        end_time = time.time() # end measuring time
        elapsed_time = (end_time - start_time) * 1000 # calculate elapsed time in milliseconds
        print(f"Total time taken: {elapsed_time:.2f} ms")
        # hasht.print_table()

    elif ds_value == '1':
        print("BST")
        input_op = reading_input(inputfile)
        start_time = time.time()
        bst.BST(input_op)
        end_time = time.time() # end measuring time
        elapsed_time = (end_time - start_time) * 1000 # calculate elapsed time in milliseconds
        print(f"Total time taken: {elapsed_time:.2f} ms")

    elif ds_value == '2':
        print("Splay tree")
        input_op = reading_input(inputfile)
        start_time = time.time()
        splay_tree.Splay(input_op)
        end_time = time.time() # end measuring time
        elapsed_time = (end_time - start_time) * 1000 # calculate elapsed time in milliseconds
        print(f"Total time taken: {elapsed_time:.2f} ms")


    elif ds_value == '3':
        print("Skip list")
        input_op = reading_input(inputfile)
        start_time = time.time()
        skip_list.SkipList(input_op)
        end_time = time.time() # end measuring time
        elapsed_time = (end_time - start_time) * 1000 # calculate elapsed time in milliseconds
        print(f"Total time taken: {elapsed_time:.2f} ms")


    elif ds_value == '4':
        print("Red-Black Tree")
        input_op = reading_input(inputfile)
        start_time = time.time()
        tree.RBT(input_op)
        end_time = time.time() # end measuring time
        elapsed_time = (end_time - start_time) * 1000 # calculate elapsed time in milliseconds
        print(f"Total time taken: {elapsed_time:.2f} ms")
