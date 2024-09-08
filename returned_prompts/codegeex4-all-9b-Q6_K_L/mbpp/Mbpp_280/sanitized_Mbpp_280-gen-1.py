def sequential_search(arr, el):
    for i, val in enumerate(arr):
        if val == el:
            return (True, i)
    return (False, -1)