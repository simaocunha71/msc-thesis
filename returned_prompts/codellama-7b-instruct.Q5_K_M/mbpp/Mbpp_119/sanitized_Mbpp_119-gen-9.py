def search(arr):
    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            continue
        elif arr[i] == arr[i - 1]:
            return arr[i]
    return arr[-1]