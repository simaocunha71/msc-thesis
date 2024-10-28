def sequential_search(arr, ele):
    if ele in arr:
        return (True, arr.index(ele))
    else:
        return (False, -1)