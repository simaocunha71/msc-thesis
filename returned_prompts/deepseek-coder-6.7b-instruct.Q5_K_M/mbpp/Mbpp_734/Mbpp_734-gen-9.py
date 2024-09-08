
def sum_Of_Subarray_Prod(l):
    sum_prod = 0
    n = len(l)
    for i in range(n):
        sum_prod += (l[i] * (i+1) * (n-i))
    return sum_prod

print(sum_Of_Subarray_Prod([1,2,3]))

Explanation:

The function works by iterating through the list and for each element, it calculates the product of that element and the length of the subarray it can contribute to. The subarray it contributes to starts at the element itself and goes up to the end of the list. The length of the subarray it contributes to is (i+1) and (n-i), where i is the index of the element in the list. The sum of products of all possible sublists can be calculated by summing up these products for all elements in the list.

This solution is based on the fact that for each element in the list, it contributes to the product of all subarrays that include that element. The length of the subarray it contributes to is (i+1) and (n-i) where i is the index of the element in the list. The product of the element and the length of the subarray it contributes to is the product of the element and the number of subarrays it contributes to. This product is added to the sum of products for all elements in the list. At the end, the sum of products is returned.

This solution has a time complexity of O(n) where n is the length of the list.
"""

# 