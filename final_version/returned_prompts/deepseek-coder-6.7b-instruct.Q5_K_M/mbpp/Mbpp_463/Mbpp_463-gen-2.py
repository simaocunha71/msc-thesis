"""
The function works by keeping track of the maximum and minimum product ending at each position. The minimum product is needed because a negative number multiplied by a negative number can become a large positive number.

We initialize max_product and min_product to the first number of the array.

For each number, we update max_product and min_product:

- max_product[i] = max(nums[i], max_product[i-1] * nums[i], min_product[i-1] * nums[i])
- min_product[i] = min(nums[i], max_product[i-1] * nums[i], min_product[i-1] * nums[i])

Finally, we return the maximum value in max_product.
"""

def max_subarray_product(nums):
    if not nums:
        return 0

    max_product = [0]*len(nums)
    min_product = [0]*len(nums)
    max_product[0] = min_product[0] = nums[0]
    for i in range(1, len(nums)):
        if nums[i] > 0:
            max_product[i] = max(nums[i], max_product[i-1] * nums[i])
            min_product[i] = min(nums[i], min_product[i-1] * nums[i])
        else:
            max_product[i] = max(nums[i], min_product[i-1] * nums[i])
            min_product[i] = min(nums[i], max_product[i-1] * nums[i])

    return max(max_product)


assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
assert max_subarray_product([-4, -3, -2]) == -6
assert max_subarray_product([-4, -3, 0, 2]) == 6
assert max_subarray_product([0, 0, 