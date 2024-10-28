def largest_subset(nums):
    nums.sort()
    i = 0
    count = 0
    while i < len(nums):
        while i < len(nums) - 1 and nums[i + 1] % nums[i] == 0:
            i += 1
        count += 1
        i += 1
    return count