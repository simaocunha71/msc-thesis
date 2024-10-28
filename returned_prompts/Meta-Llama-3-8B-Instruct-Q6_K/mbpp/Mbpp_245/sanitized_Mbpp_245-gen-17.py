def max_sum(arr):
    n = len(arr)
    inc = [1] * n
    dec = [1] * n
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                inc[i] = max(inc[i], inc[j] + 1)
            if arr[i] < arr[j]:
                dec[i] = max(dec[i], dec[j] + 1)
    
    max_sum = 0
    for i in range(n):
        max_sum = max(max_sum, inc[i] + dec[i] - 1)
    
    return max_sum