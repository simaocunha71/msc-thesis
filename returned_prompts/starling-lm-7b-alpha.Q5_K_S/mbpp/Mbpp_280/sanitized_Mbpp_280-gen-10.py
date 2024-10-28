def sequential_search(arr, elem):
    result = False
    pos = -1
    for i in range(len(arr)):
        if arr[i] == elem:
            result = True
            pos = i
            break
    return (result, pos)