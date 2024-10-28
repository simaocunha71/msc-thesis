def is_majority(arr, n, element):
    count = 0
    for i in range(n):
        if arr[i] == element:
            count += 1
    return count > n // 2