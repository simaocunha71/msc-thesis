def min_product_tuple(lst):
    min_product = float('inf')
    for tup in lst:
        product = tup[0] * tup[1]
        if product < min_product:
            min_product = product
    return min_product

print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]))  # Output: 8

"""
Explanation:

The function `min_product_tuple` takes a list of tuples as argument.
For each tuple in the list, it calculates the product of its elements (tup[0] * tup[1]),
and if this product is less than the current minimum product, it updates the minimum product.
Finally, it returns the minimum product.
"""
<jupyter_output>
8
<jupyter_text>
Problem 5
<jupyter_code>
