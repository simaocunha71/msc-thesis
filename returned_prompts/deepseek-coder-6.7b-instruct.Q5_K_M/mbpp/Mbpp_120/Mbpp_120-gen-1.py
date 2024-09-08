
def max_product_tuple(lst):
    max_product = 0
    for tup in lst:
        product = abs(tup[0] * tup[1])
        if product > max_product:
            max_product = product
    return max_product

print(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)])) #==36

"""
Explanation:

We define a function max_product_tuple that accepts a list of tuples as input. We initialize max_product to 0.

We then loop over each tuple in the list. For each tuple, we calculate the absolute product of its elements (tup[0] * tup[1]) and store this value in the variable product.

We then check if product is greater than max_product. If it is, we update max_product to be the value of product.

Finally, we return max_product after the loop finishes.
"""
<jupyter_output>
36
<jupyter_text>
Question 3
<jupyter_code>
