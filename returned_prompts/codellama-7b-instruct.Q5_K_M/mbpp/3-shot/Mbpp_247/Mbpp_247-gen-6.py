
def lps(str):
  if len(str) == 0:
    return 0
  dp = [0]*(len(str))
  max_length = 0
  for i in range(len(str)):
    for j in range(i+1, len(str)):
      if str[i] == str[j]:
        if j - i == 1:
          dp[j] = 2
        else:
          dp[j] = dp[j-1] + 2
        if dp[j] > max_length:
          max_length = dp[j]
  return max_length


