def max_sum(arr):
    n = len(arr)
    if n == 0:
        return 0
    elif n == 1:
        return arr[0]
    elif n == 2:
        return max(arr[0], arr[1])

    # Initialize arrays to store maximum sum of increasing and decreasing subsequences
    inc = [0] * n
    dec = [0] * n

    # Initialize the first element of increasing subsequence as the first element of the array
    inc[0] = arr[0]

    # Find maximum sum of increasing subsequences
    for i in range(1, n):
        inc[i] = max(inc[i - 1], inc[i] + arr[i])

    # Initialize the last element of decreasing subsequence as the last element of the array
    dec[n - 1] = arr[n - 1]

    # Find maximum sum of decreasing subsequences
    for i in range(n - 2, -1, -1):
        dec[i] = max(dec[i + 1], dec[i] + arr[i])

    # Find the maximum sum of bitonic subsequence
    max_sum = 0
    for i in range(n - 1):
        max_sum = max(max_sum, inc[i] + dec[i + 1])

    return max_sum