def sequential_search(arr, element):
    for index, value in enumerate(arr):
        if value == element:
            return True, index
    return False, -1
