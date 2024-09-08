def max_product(arr):
    n = len(arr)

    if n < 1:
        return 0

    max_end = [0] * n
    min_end = [0] * n

    max_end[0] = min_end[0] = arr[0]

    for i in range(1, n):
        if arr[i] > 0:
            max_end[i] = max(arr[i], max_end[i-1]*arr[i])
            min_end[i] = min(arr[i], min_end[i-1]*arr[i])
        else:
            max_end[i] = max(arr[i], min_end[i-1]*arr[i])
            min_end[i] = min(arr[i], max_end[i-1]*arr[i])

    return max(max_end)

print(max_product([3, 100, 4, 5, 150, 6]))  # should return 3000

"""
This solution has a time complexity of O(n) as it makes a single pass through the array. The space complexity is also O(n) as it uses two arrays to store the maximum and minimum product ending at each position.
"""
<jupyter_output>
3000
<jupyter_text>
Problem 4: [Array Pair Sum Divisible by K](https://www.hackerrank.com/challenges/divisible-sum-pairs/problem)Given an array of integers and a positive integer k, determine the number of (i, j) pairs where i < j and ar[i] + ar[j] is divisible by k.
<jupyter_code>
def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (ar[i] + ar[j]) % k == 0:
                count += 1
    return count

n = 6
k = 3
ar = [1, 3,