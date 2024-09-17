def last(array, target):
    for i in range(len(array) - 1, -1, -1):
        if array[i] == target:
            return i
    return -1