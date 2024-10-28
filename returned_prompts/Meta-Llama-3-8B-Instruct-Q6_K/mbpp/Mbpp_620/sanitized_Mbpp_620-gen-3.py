def largest_subset(nums):
    nums.sort()
    max_size = 1
    for i in range(1, len(nums)):
        if nums[i] % nums[i-1] == 0:
            max_size += 1
        else:
            break
    return max_size