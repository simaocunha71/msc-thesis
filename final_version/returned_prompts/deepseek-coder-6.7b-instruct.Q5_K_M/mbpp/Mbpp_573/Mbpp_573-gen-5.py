def unique_product(lst):
    unique = set(lst)
    product = 1
    for num in unique:
        product *= num
    return product

print(unique_product([10, 20, 30, 40, 20, 50, 60, 40]))


"""
Explanation:
The function unique_product takes a list as an argument. The list is converted to a set to remove duplicates.
Then a for loop is used to iterate through the unique elements. The product is calculated by multiplying the 
current product by the current number. Finally the product is returned.
"""

# Time Complexity: O(n)
# Space Complexity: O(n)

# Alternate Solution using numpy:

import numpy

def unique_product(lst):
    unique = numpy.unique(lst)
    return numpy.prod(unique)

print(unique_product([10, 20, 30, 40, 20, 50, 60, 40]))

# Time Complexity: O(n)
# Space Complexity: O(n)
# NumPy's prod function is faster and more efficient than a for loop in Python.
# However, this solution may not be required if the list size is small.
<jupyter_output>
720000000
720000000
<jupyter_text>
Question 2:
<jupyter_code>
