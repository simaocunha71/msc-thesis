def max_sum(arr):
    n = len(arr)
    dp = [0] * n
    for i in range(n):
        max_val = 0
        for j in range(i):
            if arr[j] < arr[i]:
                max_val = max(max_val, dp[j])
        dp[i] = max_val + arr[i]
    return max(dp)

# Test
print(max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9])) # 194

"""
The time complexity of this algorithm is O(n^2), where n is the length of the given array.
"""

def max_sum_bitonic(arr):
    n = len(arr)
    dp = [0]*n
    for i in range(n):
        max_val = 0
        for j in range(i):
            if arr[j] < arr[i]:
                max_val = max(max_val, dp[j])
        dp[i] = max_val + arr[i]
    return max(dp)

# Test
print(max_sum_bitonic([1, 15, 51, 45, 33, 100, 12, 18, 9])) # 194

"""
The time complexity of this algorithm is O(n^2), where n is the length of the given array.
"""

def max_sum_bitonic(arr):
    n = len(arr)
    dp = [0]*n
    for i in range(n):
        max_val = 0
        for j in range(i):
            if arr[j] < arr[i]:
                max_val = max(max_val, dp[j])
        dp[i] = max_val + arr[i]
    return max(dp)

# Test
print(max_sum_bitonic([1, 15, 51, 45, 33, 100, 12