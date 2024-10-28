def max_sum(arr):
    n = len(arr)
    if n == 0:
        return 0
    elif n == 1:
        return arr[0]

    # Initialize arrays to store the maximum sum of increasing and decreasing subsequences
    inc = [0] * n
    dec = [0] * n

    # Initialize the first element of inc array
    inc[0] = arr[0]

    # Fill the inc array with the maximum sum of increasing subsequences ending at each index
    for i in range(1, n):
        inc[i] = arr[i]
        for j in range(i):
            if arr[i] > arr[j] and inc[i] < inc[j] + arr[i]:
                inc[i] = inc[j] + arr[i]

    # Initialize the last element of dec array
    dec[n-1] = arr[n-1]

    # Fill the dec array with the maximum sum of decreasing subsequences ending at each index
    for i in range(n-2, -1, -1):
        dec[i] = arr[i]
        for j in range(i+1, n):
            if arr[i] > arr[j] and dec[i] < dec[j] + arr[i]:
                dec[i] = dec[j] + arr[i]

    # Find the maximum sum of bitonic subsequences
    max_sum = 0
    for i in range(n-1):
        max_sum = max(max_sum, inc[i] + dec[i+1])

    return max_sum