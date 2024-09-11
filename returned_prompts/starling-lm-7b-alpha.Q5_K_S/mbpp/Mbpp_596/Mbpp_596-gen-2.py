from sys import getsizeof

def set_size(s):
    return getsizeof(s)

# assert set_size(set(["A", 1, "B", 2, "C", 3]) ) == sys.getsizeof(set(["A", 