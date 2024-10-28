def find_min_diff(nums: list, n: int) -> int:
    nums.sort()
    min_diff = nums[1] - nums[0]
    for i in range(1, n-1):
        min_diff = min(min_diff, nums[i+1] - nums[i])
    return min_diff