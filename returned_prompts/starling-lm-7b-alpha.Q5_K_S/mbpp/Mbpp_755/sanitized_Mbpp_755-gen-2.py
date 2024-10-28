def second_smallest(nums):
    if len(nums) < 2:
        raise ValueError("List must contain at least two distinct elements")
    nums.sort()
    return nums[1]