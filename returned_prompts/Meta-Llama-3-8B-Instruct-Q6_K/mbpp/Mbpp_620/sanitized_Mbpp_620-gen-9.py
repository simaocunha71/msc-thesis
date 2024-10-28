def largest_subset(nums):
    nums.sort()
    subset = [nums[0]]
    for i in range(1, len(nums)):
        if nums[i]%subset[-1] == 0:
            subset.append(nums[i])
        else:
            break
    return len(subset) + 1