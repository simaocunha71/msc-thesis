def sequential_search(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return (True, i)
    return (False, -1)  # or return (False, -1) if you prefer this style