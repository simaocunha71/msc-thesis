def max_product_tuple(lst):
    max_prod = 0
    for tup in lst:
        prod = abs(tup[0]*tup[1])
        if prod > max_prod:
            max_prod = prod
    return max_prod

print(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)])) # Expected output: 36

"""
Explanation:
The function `max_product_tuple` goes through each tuple in the given list. It calculates the absolute product of the two numbers in the tuple. If this product is larger than the current maximum product, it replaces the current maximum product with this new product. At the end, it returns the maximum product.
"""
<jupyter_output>
36
<jupyter_text>
Problem 2:
<jupyter_code>
