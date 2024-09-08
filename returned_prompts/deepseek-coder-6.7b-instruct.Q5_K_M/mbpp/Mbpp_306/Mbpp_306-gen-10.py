
def max_sum_increasing_subseq(arr, n, k, i):
    if i > n or i < 0 or k > n or k < 0:
        return -1

    dp = [0]*n
    dp[i] = arr[i]
    max_sum = dp[i]

    for j in range(i+1, n):
        for x in range(i, j):
            if arr[j] > arr[x]:
                dp[j] = max(dp[j], dp[x]+arr[j])
        max_sum = max(max_sum, dp[j])

    return max_sum + arr[k]


print(max_sum_increasing_subseq([1, 101, 2, 3, 100, 4, 5 ], 7, 4, 6))


"""
This solution uses a dynamic programming approach to find the maximum sum of increasing subsequences. The dp array stores the maximum sum of subsequences ending at each index. The maximum sum of subsequences is then calculated by iterating through the dp array.

The time complexity of this solution is O(n^2) because of the double loop, where n is the length of the array. The space complexity is also O(n) for the dp array.
"""

# https://www.techiedelight.com/maximum-sum-increasing-subsequence-including-given-element/
<jupyter_output>
<empty_output>
<jupyter_text>
Question 4
<jupyter_code>
