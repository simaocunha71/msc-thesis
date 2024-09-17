def is_majority(arr: list, n: int, element: int) -> bool:
    count = 0
    for i in range(n):
        if arr[i] == element:
            count += 1
    if count > n/2:
        return True
    else:
        return False

