def min_product_tuple(lst):
    return min([x * y for (x, y) in lst])

print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]))

#Output: 8

#Explanation: The minimum product from the pairs of tuples within the list is obtained by multiplying 1 and 8, which equals 8.

"""
Alternatively,

You can sort the list based on the product of tuples and return the first value from the sorted list.

def min_product_tuple(lst):
    return sorted(lst, key=lambda x: x[0]*x[1])[0][0]*sorted(lst, key=lambda x: x[0]*x[1])[0][1]

print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]))

#Output: 8
"""
<jupyter_output>
8
<jupyter_text>
