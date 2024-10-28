def last(sorted_array, target):
    for i in range(len(sorted_array) - 1, -1, -1):
        if sorted_array[i] == target:
            return i
    return -1