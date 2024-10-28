import sys
def tuple_size(tup):
    return sys.getsizeof(tup)  # returns the size of the tuple in bytes
    # alternative: return sum(sys.getsizeof(i) for i in tup)  # returns the sum of sizes of all elements in the tuple in bytes