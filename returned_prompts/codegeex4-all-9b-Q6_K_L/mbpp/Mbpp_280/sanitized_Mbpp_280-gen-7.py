def sequential_search(arr, elem):
    if elem in arr:
        return (True, arr.index(elem))
    else:
        return (False, -1)