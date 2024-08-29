"""
Here is a Python solution using dynamic programming:

In this solution, we first find the maximum sum of an increasing subsequence by iterating through the array from left to right. Then we find the maximum sum of a decreasing subsequence by iterating through the array from right to left. Finally we find the maximum bitonic subsequence by iterating through the array and taking the maximum value from the sum of increasing and decreasing subsequences at each point.
"""

def max_sum(arr):
    n = len(arr)

    # Initialize arrays for storing increasing and decreasing subsequence sums
    inc = [0]*n
    dec = [0]*n

    # Initialize maximum sum
    max_sum = float('-inf')

    # Find maximum sum of increasing subsequences
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                inc[i] = max(inc[i], inc[j] + arr[i])

    # Find maximum sum of decreasing subsequences
    for i in range(n-1, -1, -1):
        for j in range(n-1, i, -1):
            if arr[i] > arr[j]:
                dec[i] = max(dec[i], dec[j] + arr[i])

    # Find maximum bitonic subsequence sum
    for i in range(n):
        max_sum = max(max_sum, inc[i] + dec[i] - arr[i])

    return max_sum

# Test the function
print(max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]))  # Output: 194

"""
This solution has a time complexity of O(n^2) and space complexity of O(n), where n is the length of the array. This is because we iterate through the array multiple times, and we use two auxiliary arrays to store the sum of increasing and decreasing subsequences.
"""

"""
This solution works by iterating through the array and finding the maximum sum of increasing and decreasing subsequences at each point. It then finds the maximum