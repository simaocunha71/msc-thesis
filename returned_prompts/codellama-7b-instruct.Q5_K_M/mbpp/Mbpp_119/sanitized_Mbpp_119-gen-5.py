def search(arr):
    for i in range(0, len(arr), 2):
        if arr[i] != arr[i+1]:
            return arr[i]
    return arr[-1]