def tuple_modulo(t1, t2):
    return tuple(a % b for a, b in zip(t1, t2))

print(tuple_modulo((10, 4, 5, 6), (5, 6, 7, 5)))

# Output:
# (0, 4, 5, 1)

# Explanation:
# The function `tuple_modulo` takes two tuples `t1` and `t2` as input. It uses the `zip` function to pair the elements of the tuples at the same index. It then uses a tuple comprehension to apply the modulo operator `%` to each pair of elements. The result is a new tuple of the same length as the input tuples.
<jupyter_output>
(0, 4, 5, 1)
<jupyter_text>
Question 5:
<jupyter_code>
