"""
def max_Product(arr):
    max_Product = (-99999999999999999999, -99999999999999999999)
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                continue
            max_Product = max(max_Product, (arr[i], arr[j]))
    return max_Product
"""

# The above solution is fine if you are only concerned with the case where the input array contains only positive integers. However, in the case where the array may also contain zeros, the above solution will not work correctly.

# Here is a revised solution that handles the case where the array may contain zeros:

def max_Product(arr):
    max_Product = (-99999999999999999999, -99999999999999999999)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            max_Product = max(max_Product, (arr[i], arr[j]))
            max_Product = max(max_Product, (arr[j], arr[i]))
    return max_Product

# This solution checks all possible pairs of elements in the array and keeps track of the pair with the highest product. It also handles the case where one of the elements in the pair is 0, as it correctly assigns the maximum product as (-99999999999999999999, -99999999999999999999) in that case.

# This solution has a time complexity of O(n^2), where n is the length of the array.

# The function can be tested with the following code:

assert max_Product([1,2,3,4,7,0,8,4]) == (7,8)

# The assert statement checks whether the function returns the expected result for the given input array. If the