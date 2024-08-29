def substract_elements(t1, t2):
    return tuple(i - j for i, j in zip(t1, t2))

print(substract_elements((10, 4, 5), (2, 5, 18)))

# Output: (8, -1, -13)

# Explanation:
# The function `substract_elements` takes in two tuples `t1` and `t2`. It uses the `zip` function to pair up the elements from `t1` and `t2` with the same index. It then uses a tuple comprehension to subtract the corresponding elements of `t2` from `t1` and returns the result as a new tuple.

# For example, with the input `(10, 4, 5)` and `(2, 5, 18)`, the function pairs these up as `(10, 2)`, `(4, 5)`, and `(5, 18)`. It then subtracts the corresponding elements of `(2, 5, 18)` from `(10, 4, 5)` to get `(8, -1, -13)`. This result is then returned.

# Note that the `zip` function pads the shorter tuple with `None` if the tuples have different lengths. This means that if you subtract `None` from an integer, Python will raise a `TypeError`. However, this is not what we want to happen, so we're assuming that the tuples are of equal length in our function.
<jupyter_output>
(8, -1, -13)
<jupyter_text>
2. **Create a function that takes a list of strings and returns a dictionary where the keys are the strings and the values are their corresponding lengths.**
<jupyter_code>
