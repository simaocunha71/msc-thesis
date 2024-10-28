def sequential_search(arr, elm):
    for i in range(len(arr)):
        if arr[i] == elm:
            return (True, i)
    return (False, -1)