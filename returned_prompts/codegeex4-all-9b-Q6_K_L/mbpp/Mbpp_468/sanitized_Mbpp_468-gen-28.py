def max_product(nums: list) -> int:
    dp = [0]*len(nums)
    for i in range(len(nums)):
        dp[i] = nums[i]
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j]*nums[i])
    return max(dp)