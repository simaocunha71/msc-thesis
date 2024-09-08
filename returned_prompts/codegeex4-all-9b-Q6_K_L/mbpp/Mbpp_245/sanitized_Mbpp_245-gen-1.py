def max_sum(arr):
    n = len(arr)
    if n == 0: return 0
    if n == 1: return arr[0]
    
    inc = [0] * n
    dec = [0] * n
    inc[0] = arr[0]
    dec[n-1] = arr[n-1]

    for i in range(1, n):
        inc[i] = max(inc[i-1], arr[i] + (inc[i-1] if i > 0 else 0))
    
    for i in range(n-2, -1, -1):
        dec[i] = max(dec[i+1], arr[i] + (dec[i+1] if i < n-1 else 0))
    
    max_sum = 0
    for i in range(n):
        max_sum = max(max_sum, inc[i] + dec[i] - arr[i])
    
    return max_sum