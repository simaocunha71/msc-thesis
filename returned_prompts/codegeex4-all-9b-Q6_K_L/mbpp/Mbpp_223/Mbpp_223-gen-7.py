def is_majority(arr: list, n: int, target: int) -> bool:
    if arr[n // 2] == target:
        return True
    return False

