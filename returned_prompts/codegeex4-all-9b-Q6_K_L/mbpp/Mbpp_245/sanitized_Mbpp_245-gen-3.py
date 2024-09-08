def max_sum(arr):
    n = len(arr)
    if n == 0:
        return 0
    elif n == 1:
        return arr[0]
    
    # Initialize arrays to store maximum sum of increasing and decreasing subsequences
    inc = [0] * n
    dec = [0] * n
    
    # Initialize the first element of inc array to the first element of the input array
    inc[0] = arr[0]
    
    # Initialize the maximum sum to the first element of the input array
    max_sum = arr[0]
    
    # Calculate maximum sum of increasing subsequences
    for i in range(1, n):
        inc[i] = max(arr[i], inc[i-1] + arr[i])
        max_sum = max(max_sum, inc[i])
    
    # Initialize the last element of dec array to the last element of the input array
    dec[n-1] = arr[n-1]
    
    # Calculate maximum sum of decreasing subsequences
    for i in range(n-2, -1, -1):
        dec[i] = max(arr[i], dec[i+1] + arr[i])
        max_sum = max(max_sum, dec[i])
    
    # Return the maximum sum of bitonic subsequences
    return max_sum