
def get_max_sum(n):
    if n <= 1:
        return n
    else:
        return max(get_max_sum(n/2) + get_max_sum(n/3) + get_max_sum(n/4) + get_max_sum(n/5), n)

print(get_max_sum(60))  # 106


# But this solution is not efficient as it has a high time complexity due to the repetition of calculations.
# We can use Dynamic Programming to optimize this.

def get_max_sum_dp(n):
    dp = [0]*(n+1)
    for i in range(1, n+1):
        dp[i] = max(dp[i//2] + dp[i//3] + dp[i//4] + dp[i//5], i)
    return dp[n]

print(get_max_sum_dp(60))  # 106


# Now the solution has a linear time complexity O(n), which is more efficient.

"""
Explanation:

We are given the function f(n) = max(f(n/2) + f(n/3) + f(n/4) + f(n/5), n) with base case f(n) = n for n <= 1.

The goal is to find the maximum sum that can be obtained by using the given equation.

The function is defined such that for every n, it takes the maximum sum of f(n/2), f(n/3), f(n/4), and f(n/5) and adds it to n.

We can solve this problem using dynamic programming. We start with base case values and keep adding the maximum sum of n/2, n/3, n/4, and n/5 to n.

Finally, we return the maximum sum for the given n.

This solution uses dynamic programming to avoid repetitive calculations, which improves the time complexity from exponential to linear.
"""
<jupyter_output>
106
106
<jupyter_text>
Question 3:
<