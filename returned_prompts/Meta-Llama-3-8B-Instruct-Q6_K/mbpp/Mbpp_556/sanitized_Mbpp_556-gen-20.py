def find_Odd_Pair(arr, n):
    odd_pairs = 0
    for i in range(n):
        for j in range(i+1, n):
            if (arr[i] ^ arr[j]) % 2 != 0:
                odd_pairs += 1
    return odd_pairs