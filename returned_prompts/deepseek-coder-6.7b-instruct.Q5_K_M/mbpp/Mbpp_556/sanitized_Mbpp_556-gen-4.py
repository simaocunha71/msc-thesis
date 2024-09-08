def find_Odd_Pair(arr,n):
    odd_count = 0
    even_count = 0

    for i in range(0, n):
        if (arr[i] & 1):
            odd_count += 1
        else:
            even_count += 1

    return odd_count * (odd_count - 1) // 2 + even_count * (even_count - 1) // 2