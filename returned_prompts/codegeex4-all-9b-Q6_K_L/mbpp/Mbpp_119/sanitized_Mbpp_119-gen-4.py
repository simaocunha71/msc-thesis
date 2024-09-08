def search(arr):
    if len(arr) == 1:
        return arr[0]
    for i in range(1, len(arr) - 1):
        if arr[i - 1] != arr[i] and arr[i] != arr[i + 1]:
            return arr[i]
    return arr[0] if arr[0] != arr[1] else arr[-1]