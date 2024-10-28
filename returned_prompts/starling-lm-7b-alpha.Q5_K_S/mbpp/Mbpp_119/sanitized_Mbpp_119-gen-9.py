def search(arr):
    if len(arr) == 0:
        return "Array is empty"
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        if arr[0] == arr[1]:
            return "Array contains only one element"
        else:
            return arr[0]
    for i in range(len(arr)-2):
        if arr[i+1] != arr[i] and arr[i+2] != arr[i+1]:
            return arr[i+1]
    if arr[-2] != arr[-1]:
        return arr[-1]