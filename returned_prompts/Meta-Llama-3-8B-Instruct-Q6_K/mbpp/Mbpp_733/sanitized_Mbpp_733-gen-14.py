def find_first_occurrence(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1