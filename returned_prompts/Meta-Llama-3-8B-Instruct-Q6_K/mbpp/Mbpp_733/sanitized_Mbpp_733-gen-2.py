def find_first_occurrence(sorted_array, target):
    try:
        return sorted_array.index(target)
    except ValueError:
        return -1