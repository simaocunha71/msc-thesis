def left_insertion(arr,val):
    if arr==[]:
        return 0
    if val<arr[0]:
        return 0
    if val>=arr[-1]:
        return len(arr)
    for i in range(len(arr)):
        if val<arr[i]:
            return i
    return len(arr)