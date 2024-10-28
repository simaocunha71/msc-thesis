
def find_first_occurrence(arr: list, num: int) -> int:
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == num:
            low = mid + 1
        elif arr[mid] > num:
            high = mid - 1
        else:
            return mid
    return -1


