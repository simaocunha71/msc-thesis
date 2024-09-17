def is_majority(arr, n, element):
    count = 0
    for num in arr:
        if num == element:
            count += 1
    return count > n // 2