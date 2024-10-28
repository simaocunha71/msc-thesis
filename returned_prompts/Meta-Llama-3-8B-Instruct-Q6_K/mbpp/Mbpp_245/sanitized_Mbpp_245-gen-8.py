def max_sum(arr):
    n = len(arr)
    inc = [1]*n
    dec = [1]*n
    
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                inc[i] = max(inc[i], inc[j] + 1)
            if arr[i] < arr[j]:
                dec[i] = max(dec[i], dec[j] + 1)
                
    return max(sum(inc), sum(dec)) - 1
    # since we subtracted 1 from the answer for every bitonic sequence, we need to subtract it from the total sum as well