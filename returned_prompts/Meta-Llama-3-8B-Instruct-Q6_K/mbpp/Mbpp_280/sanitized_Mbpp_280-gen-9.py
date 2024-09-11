def sequential_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return (True, i)
    return (False, -1)