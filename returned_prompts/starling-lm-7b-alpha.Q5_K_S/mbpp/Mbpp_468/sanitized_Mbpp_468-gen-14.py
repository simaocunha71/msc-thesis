def max_product(nums:list)->int:
    if len(nums) == 0:
        return 0
    dp = [1]*len(nums)
    for i in range(len(nums)-1, -1, -1):
        for j in range(i+1, len(nums)):
            if nums[j] > nums[i]:
                dp[i] = max(dp[i], dp[j]*nums[i])
    return max(dp)