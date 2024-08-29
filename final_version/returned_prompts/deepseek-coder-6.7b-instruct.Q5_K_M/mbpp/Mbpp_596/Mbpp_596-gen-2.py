
def tuple_size(t):
    return sys.getsizeof(t)

print(tuple_size(("A", 1, "B", 2, "C", 3)))
assert tuple_size(("A", 1, "B", 2, "C", 3)) == sys.getsizeof(("A", 1, "B", 2, "C", 3))

"""
Explanation:
The function tuple_size takes a tuple as input and returns the size in bytes of the tuple using the sys.getsizeof function.
The sys.getsizeof function returns the size of an object in bytes.
"""
<jupyter_output>
104
<jupyter_text>
Question 3:
<jupyter_code>
