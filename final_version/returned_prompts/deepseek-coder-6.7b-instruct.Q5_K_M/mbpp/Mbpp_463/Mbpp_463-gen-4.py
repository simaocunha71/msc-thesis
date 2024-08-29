def max_subarray_product(nums):
    if not nums:
        return 0
    max_prod, min_prod, result = nums[0], nums[0], nums[0]
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_prod, min_prod = min_prod, max_prod
        max_prod = max(nums[i], max_prod * nums[i])
        min_prod = min(nums[i], min_prod * nums[i])
        result = max(result, max_prod)
    return result


print(max_subarray_product([1, -2, -3, 0, 7, -8, -2]))

"""
Explanation:
The idea is to keep track of the maximum and minimum product up to the current index. 
For each element in the array, we calculate the maximum and minimum product ending at the current index. 
The maximum product is either the current number itself or the maximum product so far multiplied by the current number. 
The minimum product is similar, but it considers the minimum product so far as well. 
The maximum product so far is the maximum of the maximum product so far and the current maximum product. 
This is because the maximum product could be the product of the current number and the maximum product so far.
"""

# Time Complexity: O(n)
# Space Complexity: O(1)

# It is a dynamic programming problem. The main idea is to keep track of the maximum and minimum product up to the current index. 
# For each element in the array, we calculate the maximum and minimum product ending at the current index. 
# The maximum product is either the current number itself or the maximum product so far multiplied by the current number. 
# The minimum product is similar, but it considers the minimum product so far as well. 
# The maximum product so far is the maximum of the maximum product so far and the current maximum product. 
# This is because the maximum product could be the product of the current number and the maximum product so far.

# The time complexity is O(n) because we have to traverse the array once.