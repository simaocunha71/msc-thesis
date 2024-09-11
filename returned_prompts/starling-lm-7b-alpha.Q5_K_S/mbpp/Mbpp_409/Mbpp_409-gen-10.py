"""
def min_product_tuple(l):
    products = []
    for a, b in l:
        products.append(a * b)
    return min(products)
"""

def min_product_tuple(l):
    products = [a * b for a, b in l]
    return min(products)

# Test
assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 8
print("All tests passed")

# Extra
# Test for a single tuple
assert min_product_tuple((3, 4)) == 3
print("All tests passed")

# Test for an empty list
assert min_product_tuple([]) == None
print("All tests passed")

# Test for a list with one tuple
assert min_product_tuple([(5, 6)]) == 5
print("All tests passed")

# Test for a list with a tuple with only one element
assert min_product_tuple([(5,)]) == 5
print("All tests passed")

# Test for a list with a tuple with only one element
assert min_product_tuple([(5, 6)]) == 5
print("All tests passed")

# Test for a list with a tuple with zero elements
assert min_product_tuple([(5, 0, 6)]) == 0
print("All tests passed")

# Test for a list with a tuple with one element with zero value
assert min_product_tuple([(5, 0)]) == 0
print("All tests passed")

# Test for a list with a tuple with two elements with zero value
assert min_product_tuple([(0, 0)]) == 0
print("All tests passed")

# Test for a list with a tuple with one element with negative value
assert min_product_tuple([(5, -6)]) == -30
print("All tests passed")

# Test for a list with a tuple with two elements with negative value
assert min_product_tuple([(5, -6), (-7, 5)]) == -35
print("All tests passed")

# Test