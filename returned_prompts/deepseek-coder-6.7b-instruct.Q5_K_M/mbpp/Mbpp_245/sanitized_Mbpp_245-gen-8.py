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