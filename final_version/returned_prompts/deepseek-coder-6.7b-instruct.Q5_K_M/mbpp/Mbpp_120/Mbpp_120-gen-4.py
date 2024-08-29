def max_product_tuple(lst):
    max_product = 0
    for tup in lst:
        product = abs(tup[0] * tup[1])
        if product > max_product:
            max_product = product
    return max_product


print(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]))

#Output: 36


"""
Explanation:
We loop through each tuple in the list. 
For each tuple, we compute the absolute product of the two numbers. 
If this product is greater than our current maximum product, we update our maximum product.
Finally, we return the maximum product.
"""

# End of solution

# Start of solution

"""
