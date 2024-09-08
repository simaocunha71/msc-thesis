def min_product_tuple(lst):
    products = [x * y for (x, y) in lst]
    return min(products)

print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)])) # Output: 8

Explanation:
The function min_product_tuple takes a list of tuples as an argument. It calculates the product of each pair and stores these in a new list called products. Finally, it returns the smallest product from the list using the min function.
"""

