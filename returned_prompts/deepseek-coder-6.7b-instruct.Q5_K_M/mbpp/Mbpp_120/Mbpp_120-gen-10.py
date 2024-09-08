def max_product_tuple(lst):
    max_product = 0
    for tup in lst:
        product = abs(tup[0]*tup[1])
        if product > max_product:
            max_product = product
    return max_product

print(max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]))  # Output: 36

Explanation:
The function `max_product_tuple` iterates over each tuple in the list. For each tuple, it calculates the absolute product of the two numbers in the tuple (using the formula `abs(tup[0]*tup[1])`). If this product is greater than the current maximum product, it updates the maximum product. At the end of the function, it returns the maximum product.
"""

# Solving the problem using list comprehension

