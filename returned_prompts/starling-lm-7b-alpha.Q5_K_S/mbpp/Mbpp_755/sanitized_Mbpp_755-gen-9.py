def second_smallest(nums):
    nums.sort()
    if len(nums)<2:
        return "No second smallest number in the list"
    else:
        return nums[1]