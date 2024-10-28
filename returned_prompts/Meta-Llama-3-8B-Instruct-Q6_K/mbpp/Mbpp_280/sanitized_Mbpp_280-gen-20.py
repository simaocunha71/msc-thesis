def sequential_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return (True, i)
    return (False, -1)