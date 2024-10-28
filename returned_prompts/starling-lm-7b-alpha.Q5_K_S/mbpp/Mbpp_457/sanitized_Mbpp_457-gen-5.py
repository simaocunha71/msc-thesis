def Find_Min(arr):
    minlen = len(arr[0])
    for i in range(len(arr)):
        if len(arr[i]) < minlen:
            minlen = len(arr[i])
    return [minlen]