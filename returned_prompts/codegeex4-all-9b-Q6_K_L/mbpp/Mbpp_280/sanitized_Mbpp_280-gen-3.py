def sequential_search(arr, elem):
    for i, num in enumerate(arr):
        if num == elem:
            return (True, i)
    return (False, -1)