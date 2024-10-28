def find_first_occurrence(arr, target):
    try:
        return arr.index(target)
    except ValueError:
        return -1