def sequential_search(arr, element):
    if element in arr:
        return (True, arr.index(element))
    else:
        return (False, -1)