def right_insertion(arr,val):
    l = 0
    r = len(arr)-1
    while l<=r:
        m = (l+r)//2
        if arr[m]>val:
            r = m-1
        elif arr[m]==val:
            return m+1
        else:
            l = m+1
    return l