
def sequential_search(arr, ele):
    for i in range(len(arr)):
        if arr[i] == ele:
            return (True, i)
    return (False, -1)


