
def max_product_tuple(lst):
    return max(a*b for (a, b) in lst)
"""
The function max_product_tuple takes a list of tuples as input. It uses a generator expression to create a sequence of products of the tuples. This sequence is then passed to the built-in max function which returns the largest product.
"""

