def max_sum(nums: list) -> int:
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[-1] = nums[-1]
    for i in range(1, len(nums) - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            dp[i] = nums[i]
        else:
            dp[i] = max(nums[i - 1], nums[i + 1])
    return sum(dp)