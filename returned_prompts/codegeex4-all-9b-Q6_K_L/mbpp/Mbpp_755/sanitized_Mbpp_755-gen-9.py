def second_smallest(nums):
    if len(nums) < 2:
        return None
    min_num = min(nums)
    nums.remove(min_num)
    return min(nums)