def largest_subset(nums):
    nums.sort()
    count = 1
    for i in range(1, len(nums)):
        if nums[i] % nums[i-1] == 0:
            count += 1
        else:
            break
    return count