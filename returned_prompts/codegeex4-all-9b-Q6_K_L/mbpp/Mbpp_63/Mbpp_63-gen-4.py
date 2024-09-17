def max_difference(nums: list) -> int:
    max_diff = 0
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            diff = abs(nums[i][0] - nums[j][0])
            max_diff = max(max_diff, diff)
    return max_diff

