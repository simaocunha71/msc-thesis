
def largest_subset(nums:list) -> int:
    nums.sort()
    res = 1
    for i in range(1, len(nums)):
        if nums[i] % nums[i-1] == 0:
            res += 1
    return res


