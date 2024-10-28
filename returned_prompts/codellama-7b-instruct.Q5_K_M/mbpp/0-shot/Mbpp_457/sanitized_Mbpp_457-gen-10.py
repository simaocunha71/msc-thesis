def Find_Min(arr):
    if len(arr) == 0:
        return []
    return min(arr, key=len)