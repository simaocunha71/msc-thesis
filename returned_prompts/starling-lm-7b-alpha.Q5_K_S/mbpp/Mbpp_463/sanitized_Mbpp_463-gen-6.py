def max_subarray_product(nums):
    max_product = float('-inf')
    min_product = 1
    for i in range(len(nums)):
        if nums[i] < 0:
            min_product, max_product = max_product, min_product
        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])
    return max(max_product, min_product)