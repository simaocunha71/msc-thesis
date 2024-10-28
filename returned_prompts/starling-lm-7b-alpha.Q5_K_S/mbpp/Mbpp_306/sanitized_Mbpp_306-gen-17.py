def max_sum_increasing_subseq(nums:list,i:int,k:int,n:int)->int:
    dp = [0]*len(nums)
    dp[i] = nums[i]
    for j in range(i+1,n):
        if nums[j] > dp[j-1]:
            dp[j] = nums[j] + dp[j-1]
        else:
            dp[j] = nums[j]
    for j in range(i+1,n):
        if nums[j] > dp[j-1] and nums[j] < nums[k]:
            dp[j] = nums[j] + dp[j-1]
    return dp[n-1]