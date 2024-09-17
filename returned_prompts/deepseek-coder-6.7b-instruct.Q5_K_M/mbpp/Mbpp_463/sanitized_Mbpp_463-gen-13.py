def max_subarray_product(nums):
    max_end_here = max_end_so_far = 1
    for num in nums:
        max_end_here = max(1, max_end_here * num)
        min_end_here = min(1, min_end_here * num)
        if num > 0:
            max_end_so_far = max(max_end_so_far, max_end_here)
        else:
            max_end_so_far = max(max_end_so_far, min_end_here)
    return max_end_so_far