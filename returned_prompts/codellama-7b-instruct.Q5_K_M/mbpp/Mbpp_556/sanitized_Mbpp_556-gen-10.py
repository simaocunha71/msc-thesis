def find_Odd_Pair(arr, N):
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            if (arr[i] ^ arr[j]) % 2 == 1:
                count += 1
    return count