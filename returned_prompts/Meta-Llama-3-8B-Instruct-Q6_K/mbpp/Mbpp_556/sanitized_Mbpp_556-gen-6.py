def find_Odd_Pair(arr, n):
    odd_count = 0
    for i in range(n):
        for j in range(i+1, n):
            if (arr[i] ^ arr[j]) % 2 != 0:
                odd_count += 1
    return odd_count