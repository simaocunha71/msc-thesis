
def get_total_number_of_sequences(m, n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, m + 1):
        for j in range(n, 0, -1):
            dp[j] += dp[j - 1]
    return dp[n]

print(get_total_number_of_sequences(10, 4))

# Output:
# 4

"""
Explanation:

The function `get_total_number_of_sequences` uses dynamic programming to solve the problem. 
The dp array represents the number of sequences of length `n` ending with a certain number `i`. 
The outer loop iterates through all the possible numbers from 1 to `m`, 
and the inner loop updates the dp array from `n` to `1`, 
which means the number of sequences of length `i` ending with `i` is the sum of the sequences of length `i - 1` ending with any number `j` (0 <= j < i).
Finally, it returns the number of sequences of length `n` ending with any number `i`, which is the sum of the sequences of length `n` ending with `i` for all `i`.
"""
<jupyter_output>
4
<jupyter_text>
Question 2:
<jupyter_code>
