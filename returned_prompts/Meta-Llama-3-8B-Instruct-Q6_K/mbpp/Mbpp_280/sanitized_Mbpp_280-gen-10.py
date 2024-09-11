def sequential_search(arr, elem):
    for i, val in enumerate(arr):
        if val == elem:
            return (True, i)
    return (False, -1)  # return False if not found and -1 as index