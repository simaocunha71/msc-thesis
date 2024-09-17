def max_subarray_product(nums):
    prod = cur_max = cur_min = nums[0]
    for i in nums[1:]:
        cur_max = max(cur_max*i, cur_min*i, i)
        cur_min = min(cur_min*i, cur_max*i, i)
        prod = max(prod, cur_max)
    return prod