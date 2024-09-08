
def combinations_colors(color_list, n):
    # Import combinations from itertools
    from itertools import product
    # Use product to generate all combinations
    return list(product(*([color_list]*n)))

print(combinations_colors(["Red","Green","Blue"],1))

"""
The function `combinations_colors` uses the `product` function from `itertools` module to generate all combinations. The `product` function takes a list of iterables as arguments and returns cartesian products of the iterables. In this case, we want to generate combinations of colors, so we pass `color_list` repeated `n` times to `product`.

The `*` operator is used to unpack the list `color_list` `n` times. This is necessary because `product` expects a list of iterables, and `color_list` needs to be passed as an argument `n` times.

Finally, the result is converted to a list and returned.
"""
<jupyter_output>
[('Red',), ('Green',), ('Blue',)]
<jupyter_text>
Question 2:
<jupyter_code>
