def pair_xor_Sum(arr, n):
    sum = 0
    for i in range(0, 32):
        c = 0
        for j in range(0, n):
            if ((arr[j] & (1 << i))):
                c += 1
        sum += c * (n - c) * 2
    return sum
arr = [5,9,7,6]
n = len(arr)