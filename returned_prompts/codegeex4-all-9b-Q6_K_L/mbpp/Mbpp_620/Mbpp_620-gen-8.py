def largest_subset(nums: list) -> int:
    nums.sort()
    subsets = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                subsets[i] = max(subsets[i], subsets[j] + 1)
    return max(subsets)

