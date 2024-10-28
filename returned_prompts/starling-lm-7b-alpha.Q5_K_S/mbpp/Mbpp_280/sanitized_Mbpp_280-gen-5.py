def sequential_search(arr, element):
    bool = False
    index = -1
    for i in range(len(arr)):
        if arr[i] == element:
            bool = True
            index = i
    return (bool, index)