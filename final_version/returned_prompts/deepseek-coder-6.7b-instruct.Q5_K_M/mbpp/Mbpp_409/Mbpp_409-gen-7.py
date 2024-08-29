def min_product_tuple(lst):
    return min([x*y for (x, y) in lst])

print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]))
<jupyter_output>
8
<jupyter_text>
Question 5:Write a Python function to find the maximum product from the pairs of tuples within a given list.
<jupyter_code>
