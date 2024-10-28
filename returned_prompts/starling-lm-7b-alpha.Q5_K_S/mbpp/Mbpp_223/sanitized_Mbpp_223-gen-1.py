def is_majority(arr, n, elem):
    left = 0
    right = n - 1
    while left < right:
        mid = (left + right + 1) // 2
        if arr[mid] == elem:
            break
        elif arr[mid] > elem:
            right = mid - 1
        else:
            left = mid
    left_cnt = 0
    right_cnt = 0
    for i in range(left, n):
        if arr[i] == elem:
            left_cnt += 1
        else:
            break
    for i in range(right, -1, -1):
        if arr[i] == elem:
            right_cnt += 1
        else:
            break
    return left_cnt > n // 2 or right_cnt > n // 2