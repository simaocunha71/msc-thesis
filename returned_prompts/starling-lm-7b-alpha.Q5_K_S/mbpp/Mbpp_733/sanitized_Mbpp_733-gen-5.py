def find_first_occurrence(array, target):
    array_length = len(array)
    for i in range(array_length):
        if array[i] == target:
            return i
    return -1