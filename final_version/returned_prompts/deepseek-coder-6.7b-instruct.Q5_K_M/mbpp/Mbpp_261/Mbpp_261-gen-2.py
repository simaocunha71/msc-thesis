
def division_elements(t1, t2):
    return tuple(x // y for x, y in zip(t1, t2))

print(division_elements((10, 4, 6, 9),(5, 2, 3, 3)))

"""
Here, we use the zip function to pair up elements from the two tuples at the same index. Then we use a generator expression to perform the division operation element-wise. We return the result as a new tuple.
"""
<jupyter_output>
(2, 2, 2, 3)
<jupyter_text>
