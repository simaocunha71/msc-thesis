def max_sum(arr):
    n = len(arr)
    max_sum = [0] * n
    max_sum[0] = arr[0]
    
    for i in range(1, n):
        max_sum[i] = max(max_sum[i-1], arr[i] + (max_sum[i-2] if i >= 2 else 0))
    
    max_sum_decreasing = [0] * n
    max_sum_decreasing[n-1] = arr[n-1]
    
    for i in range(n-2, -1, -1):
        max_sum_decreasing[i] = max(max_sum_decreasing[i+1], arr[i] + (max_sum_decreasing[i+2] if i+2 < n else 0))
    
    max_sum_bitonic = [0] * n
    for i in range(n):
        max_sum_bitonic[i] = max(max_sum[i], max_sum_decreasing[n-1-i])
    
    return max(max_sum_bitonic)