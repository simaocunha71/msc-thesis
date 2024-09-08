def max_sum(arr):
    n = len(arr)
    
    # Initialize maxInc and maxDec arrays
    maxInc = [0] * n
    maxDec = [0] * n
    
    # Fill maxInc array
    for i in range(n):
        maxInc[i] = arr[i]
        for j in range(i):
            if arr[i] > arr[j]:
                maxInc[i] = max(maxInc[i], maxInc[j] + arr[i])
    
    # Fill maxDec array
    for i in range(n-1, -1, -1):
        maxDec[i] = arr[i]
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                maxDec[i] = max(maxDec[i], maxDec[j] + arr[i])
    
    # Find the maximum sum of a bitonic subsequence
    maxSum = 0
    for i in range(n):
        maxSum = max(maxSum, maxInc[i] + maxDec[i] - arr[i])
    
    return maxSum