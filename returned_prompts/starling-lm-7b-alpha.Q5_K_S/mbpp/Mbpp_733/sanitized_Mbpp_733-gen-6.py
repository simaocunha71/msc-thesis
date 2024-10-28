def find_first_occurrence(arr, target):
    """Find the first occurrence of a given number in a sorted array."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            right = mid - 1  # The target is found, so move left to find the first occurrence.
        elif arr[mid] < target:
            left = mid + 1  # The target is greater than the current mid element, so move right.
        else:
            right = mid - 1  # The target is less than the current mid element, so move left.
    return left