def sequential_search(array, element):
    result = (False, -1)
    for i in range(len(array)):
        if array[i] == element:
            result = (True, i)
    return result