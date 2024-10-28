import sys
def tuple_size(t):
    size = sys.getsizeof(t)
    for item in t:
        size += sys.getsizeof(item)
    return size