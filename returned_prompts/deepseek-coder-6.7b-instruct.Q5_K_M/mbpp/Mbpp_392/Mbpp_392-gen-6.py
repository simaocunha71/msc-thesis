def get_max_sum(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = max(dp[i//2] + dp[i//3] + dp[i//4] + dp[i//5], i)
    return dp[n]

print(get_max_sum(60))  # Output: 106


"""
The function uses a dynamic programming approach to solve the problem.
It calculates the maximum sum for each number up to n by using the given equation.
The maximum sum for each number is calculated by taking the maximum sum for its divisors plus the number itself.
"""
<jupyter_output>
106
<jupyter_text>
Question 2:
<jupyter_code>
