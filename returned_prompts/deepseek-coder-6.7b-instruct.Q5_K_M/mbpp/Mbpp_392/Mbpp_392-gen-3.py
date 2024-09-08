
def get_max_sum(n):
    if n <= 1:
        return n

    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = max(dp[i//2] + dp[i//3] + dp[i//4] + dp[i//5], i)

    return dp[n]

print(get_max_sum(60))  # 106

"""
This function works by using dynamic programming to store previously computed sums. It starts by initializing an array dp of size n+1, all elements to 0. Then it fills the dp array in a bottom-up manner, where dp[i] represents the maximum sum we can get by using i as the number. The dp[i] is computed by taking the maximum of dp[i//2] + dp[i//3] + dp[i//4] + dp[i//5] and i. Finally, it returns the nth element of the dp array, which represents the maximum sum we can get by using n as the number.
"""

# Time Complexity: O(n)
# Space Complexity: O(n)
<jupyter_output>
106
<jupyter_text>
Question 2
<jupyter_code>
