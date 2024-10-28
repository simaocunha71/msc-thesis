def max_subarray_product(nums):
    max_product = nums[0]
    min_product = nums[0]
    max_global = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product
        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])
        max_global = max(max_global, max_product)
    return max_global