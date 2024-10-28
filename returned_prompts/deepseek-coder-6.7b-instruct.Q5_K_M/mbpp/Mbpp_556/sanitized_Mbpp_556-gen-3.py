def find_Odd_Pair(arr, n):
    odd = 0
    even = 0
    for i in range(0, n):
        if (arr[i] & 1):
            odd += 1
        else:
            even += 1
    return odd * even