
def Find_Min(arr):
    min_len = len(arr[0])
    min_sublist = arr[0]
    for i in range(1,len(arr)):
        if len(arr[i]) < min_len:
            min_len = len(arr[i])
            min_sublist = arr[i]
    return min_sublist


