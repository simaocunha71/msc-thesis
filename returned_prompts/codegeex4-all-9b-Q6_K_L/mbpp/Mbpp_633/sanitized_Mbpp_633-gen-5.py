def pair_xor_Sum(arr, N):
    sum = 0
    for i in range(N):
        for j in range(i + 1, N):
            sum += arr[i] ^ arr[j]
    return sum