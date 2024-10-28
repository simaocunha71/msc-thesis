
def find_min_diff(nums: list, n: int) -> int:
    nums.sort()
    if len(nums) == 1:
        return 0
    return min(nums[i+1] - nums[i] for i in range(len(nums)-1))


