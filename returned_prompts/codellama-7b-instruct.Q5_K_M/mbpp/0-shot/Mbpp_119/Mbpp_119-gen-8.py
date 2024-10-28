"""
def search(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    if arr[0] != arr[1]:
        return arr[0]
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            return arr[i]
    return None
"""
