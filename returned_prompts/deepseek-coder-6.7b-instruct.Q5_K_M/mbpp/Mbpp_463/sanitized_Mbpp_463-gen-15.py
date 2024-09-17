def max_subarray_product(nums):
    n = len(nums)
    max_end_here = nums[0]
    min_end_here = nums[0]
    max_so_far = nums[0]
    for i in range(1, n):
        end_here_1 = max_end_here * nums[i]
        end_here_2 = min_end_here * nums[i]
        max_end_here = max(nums[i], end_here_1, end_here_2)
        min_end_here = min(nums[i], end_here_1, end_here_2)
        max_so_far = max(max_so_far, max_end_here)
    return max_so_far