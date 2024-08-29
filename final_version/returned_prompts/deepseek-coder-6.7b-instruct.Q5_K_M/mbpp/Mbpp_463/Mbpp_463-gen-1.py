
def max_subarray_product(nums):
    if not nums:
        return 0

    max_product = min_product = result = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product

        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])

        result = max(result, max_product)

    return result

print(max_subarray_product([1, -2, -3, 0, 7, -8, -2]))
"""
Explanation: The maximum product subarray is [7, -8, -2] which gives the result 112.
"""


