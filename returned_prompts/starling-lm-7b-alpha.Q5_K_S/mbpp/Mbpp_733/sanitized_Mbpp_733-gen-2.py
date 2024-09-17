def find_first_occurrence(arr, target):
    """
    Find the index of the first occurrence of a given number in a sorted array.
    """
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            end = mid - 1
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return start