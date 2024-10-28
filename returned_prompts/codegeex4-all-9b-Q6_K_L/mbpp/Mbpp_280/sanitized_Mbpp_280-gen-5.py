def sequential_search(arr, el):
    if el in arr:
        return (True, arr.index(el))
    else:
        return (False, -1)