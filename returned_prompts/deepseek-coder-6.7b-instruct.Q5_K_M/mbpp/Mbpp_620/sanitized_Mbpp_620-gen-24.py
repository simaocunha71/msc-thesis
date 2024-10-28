def largest_subset(arr):
  n=len(arr)
  arr.sort()
  dp=[1]*n
  for i in range(1,n):
    for j in range(i):
      if arr[i]%arr[j]==0:
        dp[i]=max(dp[i],dp[j]+1)
  return max(dp)