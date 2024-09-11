from operator import mul
from itertools import product, starmap
from functools import reduce

def large_product(list1, list2, num):
    """
    Find the largest products from two given lists, selecting one factor from each list
    """
    return list(reduce(max, starmap(mul, product(list1, list2)))[:num])

# Test
assert large_product([1, 2, 3, 4, 5, 6],[3, 6, 8, 9, 10, 6],3)==[60, 54, 50]

# Time complexity: O(N+M)
# Space complexity: O(N+M)

# Reference: https://stackoverflow.com/questions/3898820/calculate-cartesian-product-of-two-lists-in-python
# Reference: https://stackoverflow.com/questions/3202091/fastest-way-to-multiply-two-lists-together-in-python


"""
The complexity is O(N * M) because we need to calculate the product of each pair of elements in two lists.
The space complexity is O(N + M) because we need to store the result list.

For time complexity,
1. In the worst case, we need to calculate the product of each pair of elements in two lists, which is O(N * M).
2. The function reduce() is used to find the maximum of all the products, which has a time complexity of O(log(N * M)).
3. The function starmap() is used to generate all the products of the two lists, which has a time complexity of O(N * M).
4. The function product() is used to generate all the Cartesian products of the two lists, which has a time complexity of O(N * M).
5. The function max() is used to find the maximum of all the products, which has a time complexity of O(N * M).
6. The function slice[:num] is used to select the first num products, which has a time complexity of O(N * M).
7. The function list() is used to convert the result to a list