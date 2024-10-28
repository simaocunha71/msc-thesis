def is_majority(arr: list, n: int, el: int) -> bool:
    count = 0
    for i in range(n):
        if arr[i] == el:
            count += 1
            if count > n / 2:
                return True
    return False

