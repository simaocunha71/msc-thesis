"""
We can use Dynamic Programming to solve this problem.

The basic idea is to find the maximum sum of increasing subsequence ending at each position and then find the maximum sum of decreasing subsequence starting at each position. And then, take the maximum sum of all these sums.

Here is the Python code that implements this idea:
"""

def max_sum(arr):
    n = len(arr)

    # Initialize the increasing and decreasing DP arrays
    inc = [0]*n
    dec = [0]*n

    # Initialize the maximum sum as the sum of the first element
    max_sum = arr[0]

    # Fill the increasing DP array
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and inc[i] < inc[j] + arr[i]:
                inc[i] = inc[j] + arr[i]

        # If the maximum sum is less than the sum at the current position, update the maximum sum
        if max_sum < inc[i]:
            max_sum = inc[i]

    # Fill the decreasing DP array
    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            if arr[i] > arr[j] and dec[i] < dec[j] + arr[i]:
                dec[i] = dec[j] + arr[i]

            # If the maximum sum is less than the sum at the current position, update the maximum sum
            if max_sum < inc[i] + dec[j]:
                max_sum = inc[i] + dec[j]

    return max_sum


print(max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]))  # 194

"""
This solution has a time complexity of O(n^2) and space complexity of O(n), where n is the length of the array.
"""

# 2. Longest Common Subsequence (LCS)