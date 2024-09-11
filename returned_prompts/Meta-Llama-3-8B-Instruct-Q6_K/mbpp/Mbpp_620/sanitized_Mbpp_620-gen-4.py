def largest_subset(lst):
    dp = [1]*len(lst)
    for i in range(len(lst)):
        for j in range(i):
            if lst[i]%lst[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp) # Return the maximum size of subset