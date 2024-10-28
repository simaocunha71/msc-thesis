def sequential_search(arr, element):
    for i, e in enumerate(arr):
        if e == element:
            return (True, i)
    return (False, -1)  # or return (False, None) if you prefer