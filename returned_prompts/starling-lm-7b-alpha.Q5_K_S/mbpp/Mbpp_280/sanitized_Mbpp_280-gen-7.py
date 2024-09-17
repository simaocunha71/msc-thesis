def sequential_search(arr, element):
    boolean = False
    index = -1
    for i in range(len(arr)):
        if arr[i] == element:
            boolean = True
            index = i
    return (boolean, index)