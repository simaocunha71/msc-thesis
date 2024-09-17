
def max_subarray_product(nums: list) -> int:
    current_max = global_max = nums[0]
    for i in nums[1:]:
        current_max = max(i, current_max + i)
        global_max = max(global_max, current_max)
    return global_max


