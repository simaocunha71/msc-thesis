def max_sum_increasing_subseq(seq:list,i:int,k:int,n:int):
  dp = [0]*(n+1)
  dp[0] = seq[0]
  dp[1] = max(seq[0],seq[1])
  for i in range(2,n+1):
    dp[i] = max(dp[i-1],seq[i-1]+dp[i-2])
  return dp[k]