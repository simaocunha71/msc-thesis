def sequential_search(array, element):
    for i, value in enumerate(array):
        if value == element:
            return (True, i)
    return (False, -1)