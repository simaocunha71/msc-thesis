def largest_subset(nums):
    n = len(nums)
    nums.sort()
    lookup = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                lookup[i] = max(lookup[i], lookup[j] + 1)
    return max(lookup)