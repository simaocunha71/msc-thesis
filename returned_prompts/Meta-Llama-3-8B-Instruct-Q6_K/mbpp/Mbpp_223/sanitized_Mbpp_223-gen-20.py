def is_majority(arr, n, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count > n // 2