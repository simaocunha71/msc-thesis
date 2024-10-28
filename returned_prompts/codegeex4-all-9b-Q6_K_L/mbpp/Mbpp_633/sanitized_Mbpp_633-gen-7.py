def pair_xor_Sum(arr, k):
    res = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            res += arr[i] ^ arr[j]
    return res