def max_product_tuple(lst):
    max_product = float('-inf')
    for tup in lst:
        product = abs(tup[0]*tup[1])
        if product > max_product:
            max_product = product
    return max_product

print(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]))

"""
The function works by initializing a variable max_product to the lowest possible float value. Then it iterates over each tuple in the list, calculating the absolute value of their product. If this product is larger than max_product, it updates max_product. Finally, it returns the largest product.
"""
<jupyter_output>
36
<jupyter_text>
Q2.
<jupyter_code>
