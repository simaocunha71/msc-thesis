def max_subarray_product(nums):
    max_product = nums[0]
    min_product = nums[0]
    max_so_far = nums[0]
    min_so_far = nums[0]

    for i in range(1, len(nums)):
        max_product = max(nums[i], max_product*nums[i], min_product*nums[i])
        min_product = min(nums[i], max_product*nums[i], min_product*nums[i])
        max_so_far = max(max_so_far, max_product)
        min_so_far = min(min_so_far, min_product)

    return max_so_far