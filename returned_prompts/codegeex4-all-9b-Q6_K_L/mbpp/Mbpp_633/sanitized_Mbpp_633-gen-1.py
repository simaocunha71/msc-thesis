def pair_xor_Sum(arr, n): 
    xor_sum = 0
    for i in range(n): 
        for j in range(i + 1, n): 
            xor_sum += arr[i] ^ arr[j] 
    return xor_sum
arr = [5,9,7,6]
n = len(arr)