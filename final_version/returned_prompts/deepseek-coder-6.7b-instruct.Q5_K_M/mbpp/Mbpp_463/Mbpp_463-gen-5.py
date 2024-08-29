def max_subarray_product(nums):
    max_product, min_product, result = nums[0], nums[0], nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product

        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])
        result = max(result, max_product)

    return result

print(max_subarray_product([1, -2, -3, 0, 7, -8, -2]))  # 112
"""
Explanation:
The maximum product subarray is [7, -8, -2].
"""


# Time complexity: O(n)
# Space complexity: O(1)

# The function uses the concept of Dynamic Programming to keep track of the maximum and minimum product up to the current index.
# The maximum product is updated at every step by taking the maximum between the current number and the maximum product up to the previous index multiplied by the current number.
# Similarly, the minimum product is updated by taking the minimum between the current number and the minimum product up to the previous index multiplied by the current number.
# The result is the maximum of all maximum products.
# If the current number is negative, we swap the max_product and min_product as a negative number multiplied by a larger number can become a larger positive number.
# Finally, the function returns the result.


# The function takes in an array of integers, and returns the maximum product subarray.
# The function does this by iterating over the array, and at each step updating the maximum and minimum product up to the current index.
# The maximum product subarray is then the maximum of all maximum products found at each step.
# The function returns the result.
# The function runs in O(n) time, as it only needs to iterate over the array once, and in O(1) space, as it only needs to keep track of the maximum and minimum product up to the current index and the result.
