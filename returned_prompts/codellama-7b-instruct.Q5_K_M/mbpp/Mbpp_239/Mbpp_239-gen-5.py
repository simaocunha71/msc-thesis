
def get_total_number_of_sequences(m, n):
  # Edge case
  if m < 2 or n < 1:
    return 0

  # Initialize dp array
  dp = [1] * (m + 1)

  # Loop from 2 to n
  for i in range(2, n + 1):
    # Loop from 1 to m
    for j in range(1, m + 1):
      # If j is greater than i, the current element is greater than or equal to twice the previous element
      if j >= i * 2:
        # Set dp[j] to dp[j - 1]
        dp[j] = dp[j - 1]
      # Else
      else:
        # Set dp[j] to dp[j - 1] + dp[j - 2]
        dp[j] = dp[j - 1] + dp[j - 2]

  # Return dp[n]
  return dp[n]


