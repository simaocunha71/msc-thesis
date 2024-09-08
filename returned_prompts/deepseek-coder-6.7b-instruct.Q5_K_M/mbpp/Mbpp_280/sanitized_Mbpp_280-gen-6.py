def sequential_search(array, element):
    for index in range(len(array)):
        if array[index] == element:
            return (True, index)
    return (False, -1)