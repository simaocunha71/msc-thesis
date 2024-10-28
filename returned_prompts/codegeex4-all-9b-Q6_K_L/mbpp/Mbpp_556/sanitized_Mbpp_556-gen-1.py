def find_Odd_Pair(arr, k):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if (arr[i] ^ arr[j]) % 2 == 1:
                count += 1
    return count