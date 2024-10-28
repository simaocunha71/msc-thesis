def largest_subset(nums):
    nums.sort()
    max_subset = 0
    for i in range(len(nums)):
        if nums[i] % nums[i-1] == 0:
            max_subset = i + 1
    return max_subset