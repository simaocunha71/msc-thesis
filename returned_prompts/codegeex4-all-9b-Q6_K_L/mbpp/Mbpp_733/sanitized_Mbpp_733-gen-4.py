def find_first_occurrence(arr, num):
    for i, n in enumerate(arr):
        if n == num:
            return i
    return -1