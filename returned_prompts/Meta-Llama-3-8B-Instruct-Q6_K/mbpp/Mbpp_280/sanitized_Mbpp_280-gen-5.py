def sequential_search(arr, element):
    for i, val in enumerate(arr):
        if val == element:
            return (True, i)
    return (False, -1)  # element not found in the array