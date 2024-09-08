import sys

def tuple_size(tup):
    return sys.getsizeof(tup)

tup = ("A", 1, "B", 2, "C", 3)
print(tuple_size(tup))
print(sys.getsizeof(tup))
<jupyter_output>
104
104
<jupyter_text>
