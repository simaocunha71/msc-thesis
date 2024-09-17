def find_Odd_Pair(arr,n):
    odd_count = 0
    for i in range(0, n):
        for j in range(i + 1, n):
            if (arr[i] ^ arr[j]) & 1:
                odd_count += 1
    return odd_count