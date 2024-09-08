def max_sum(arr):
    n = len(arr)
    if n < 3:
        return 0
    
    # Initialize the increasing and decreasing sum array with the input array.
    inc = arr[:]
    dec = arr[:]
    
    # Find the maximum sum of increasing subsequence.
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j] and inc[i] < inc[j] + arr[i]:
                inc[i] = inc[j] + arr[i]
    
    # Find the maximum sum of decreasing subsequence.
    for i in range(n-2, -1, -1):
        for j in range(n-1, i, -1):
            if arr[i] > arr[j] and dec[i] < dec[j] + arr[i]:
                dec[i] = dec[j] + arr[i]
    
    # Find the maximum sum of bitonic subsequence.
    bitonic = [0]*n
    for i in range(n):
        bitonic[i] = inc[i] + dec[i] - arr[i]
    
    return max(bitonic)