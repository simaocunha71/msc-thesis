def pair_xor_Sum(arr, x):
    total = 0
    for i in range(len(arr)):
        total += x ^ arr[i]
    return total