def sequential_search(arr, element):
    for i, value in enumerate(arr):
        if value == element:
            return (True, i)
    return (False, -1)