def last(arr, elem):
    """
    :param arr: sorted array
    :param elem: element to search
    :return: the index of the last occurrence of elem in arr, or None if elem is not in arr.
    """
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == elem:
            left = mid + 1
        else:
            right = mid - 1
    if left < len(arr) and arr[left] == elem:
        return left
    return None