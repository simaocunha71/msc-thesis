def find_Odd_Pair(arr,n):
    arr.sort()
    start = 0
    end = n-1
    count = 0
    while start < end:
        if arr[start] ^ arr[end] % 2 == 1:
            count += 1
            start += 1
            end -= 1
        elif arr[start] ^ arr[end] % 2 == 0:
            end -= 1
    return count