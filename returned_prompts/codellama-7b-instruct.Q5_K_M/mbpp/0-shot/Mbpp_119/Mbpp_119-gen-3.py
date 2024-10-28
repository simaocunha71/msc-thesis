"""
def search(arr):
    if len(arr) == 0:
        return None
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            continue
        if arr[i+1] - arr[i] == 1:
            return arr[i+1]
    return arr[-1]
"""
