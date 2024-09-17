
def max_subarray_product(nums):
    max_val = nums[0]
    min_val = nums[0]
    max_product = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_val, min_val = min_val, max_val

        max_val = max(nums[i], max_val * nums[i])
        min_val = min(nums[i], min_val * nums[i])

        max_product = max(max_product, max_val)

    return max_product


