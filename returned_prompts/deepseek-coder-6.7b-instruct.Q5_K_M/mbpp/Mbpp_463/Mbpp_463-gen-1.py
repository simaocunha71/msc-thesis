
def max_subarray_product(nums):
    max_end_here = max_end_so_far = 1
    for num in nums:
        max_end_here = max(1, max_end_here * num)
        max_end_so_far = max(max_end_so_far, max_end_here)
    return max_end_so_far


