
def and_tuples(t1, t2):
    if len(t1) != len(t2):
        return "Tuples are not of the same length"
    return tuple(i & j for i, j in zip(t1, t2))

print(and_tuples((10, 4, 6, 9), (5, 2, 3, 3)))

# Output: (0, 0, 2, 1)

"""
This solution works by using the zip() function to combine the two tuples into pairs of elements. It then uses a generator expression to create a new tuple. It performs a bitwise AND operation (&) on each pair of elements. The result is a tuple of the bitwise AND results.
"""

"""
Another approach is to use map() function:

def and_tuples(t1, t2):
    if len(t1) != len(t2):
        return "Tuples are not of the same length"
    return tuple(map(lambda x, y: x & y, t1, t2))

print(and_tuples((10, 4, 6, 9), (5, 2, 3, 3)))

# Output: (0, 0, 2, 1)
"""

# This solution works in a similar way to the first solution, but it uses the map() function instead of a generator expression to apply the bitwise AND operation to each pair of elements.
<jupyter_output>
<empty_output>
<jupyter_text>
