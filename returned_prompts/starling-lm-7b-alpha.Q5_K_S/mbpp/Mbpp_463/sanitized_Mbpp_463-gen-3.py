def max_subarray_product(nums):
    max_product = nums[0]
    min_product = nums[0]
    cur_product = nums[0]
    for i in range(1, len(nums)):
        cur_product = max(nums[i], cur_product * nums[i], min_product * nums[i])
        max_product = max(cur_product, max_product)
        min_product = min(cur_product, min_product)
    return max_product