def division_elements(t1, t2):
    return tuple(map(lambda x, y: x / y, t1, t2))

print(division_elements((10, 4, 6, 9),(5, 2, 3, 3)))

# Output:
# (2, 2, 2, 3)

# This code works by using the map function to apply a lambda function that divides two elements from the tuples. The map function returns an iterable, so we use the tuple function to convert it back into a tuple.
<jupyter_output>
<empty_output>
<jupyter_text>
4. Find the intersection of two lists.
<jupyter_code>
