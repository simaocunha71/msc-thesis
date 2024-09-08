def max_sum(arr):
    n = len(arr)

    # Initialize variables
    inc = [0]*n
    dec = [0]*n

    # Compute increasing sum
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and inc[i] < inc[j]:
                inc[i] = inc[j]
        inc[i] += arr[i]

    # Compute decreasing sum
    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            if arr[i] > arr[j] and dec[i] < dec[j]:
                dec[i] = dec[j]
        dec[i] += arr[i]

    # Find maximum sum of bitonic subsequence
    max_sum = arr[0]
    for i in range(1, n):
        for j in range(i):
            if inc[j] + dec[i] > max_sum:
                max_sum = inc[j] + dec[i]
        if arr[i] > max_sum:
            max_sum = arr[i]

    return max_sum