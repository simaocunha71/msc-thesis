def sequential_search(arr, elem):
    for i in range(len(arr)):
        if arr[i] == elem:
            return True, i
    return False, -1


