"""
We can use the concept of dynamic programming to solve this problem. The idea is to store the results of subproblems so that they can be reused later.

Let's write the python code:
"""

# Python code
def get_max_sum(n):
    # Create a list to store the computed results
    dp = [0]*(n+1)

    # Compute the sum for all n from 1 to n
    for i in range(1, n+1):
        dp[i] = max(dp[i//2] + dp[i//3] + dp[i//4] + dp[i//5], i)
    
    # Return the maximum sum
    return dp[n]

# Testing the function
print(get_max_sum(60))  # Output: 106

"""
In the above code, we first create a list dp of size n+1 and initialize it with 0s. Then, we start from 1 and go up to n, for each number i, we calculate the sum as per the given equation and store it in dp[i]. Finally, we return dp[n] as the maximum sum.
"""

# Time Complexity: O(n)
# Space Complexity: O(n)

# This solution is efficient because it avoids the redundant computation of the same subproblem by storing its result.
# Thus, it reduces the time complexity from exponential to linear.
<jupyter_output>
<empty_output>
<jupyter_text>
Question 4
<jupyter_code>
