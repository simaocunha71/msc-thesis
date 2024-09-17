def max_sum(arr):
    n = len(arr)
    if n < 2:
        return max(arr)
    
    increasing = [0] * n
    decreasing = [0] * n
    
    increasing[0] = arr[0]
    decreasing[n-1] = arr[n-1]
    
    for i in range(1, n):
        increasing[i] = max(increasing[i-1], arr[i])
    for i in range(n-2, -1, -1):
        decreasing[i] = max(decreasing[i+1], arr[i])
    
    max_sum = 0
    for i in range(n):
        max_sum = max(max_sum, increasing[i] + decreasing[i])
    
    return max_sum