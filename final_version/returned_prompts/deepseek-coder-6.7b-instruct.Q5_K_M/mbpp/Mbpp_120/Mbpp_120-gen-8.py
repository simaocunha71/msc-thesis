def max_product_tuple(lst):
    max_product = 0
    for tup in lst:
        product = abs(tup[0]*tup[1])
        if product > max_product:
            max_product = product
    return max_product

print(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]))

# Output: 36
<jupyter_output>
36
<jupyter_text>
Q2.
<jupyter_code>
