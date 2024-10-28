def sequential_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return (True, i)
    return (False, -1)  # Return false and -1 if the element is not found