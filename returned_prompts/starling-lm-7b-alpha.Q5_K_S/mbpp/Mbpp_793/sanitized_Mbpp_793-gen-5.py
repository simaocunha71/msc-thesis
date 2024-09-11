def last(arr,key):
    low,high = 0,len(arr)-1
    while low<high:
        mid = (low+high)//2
        if arr[mid]>key:
            high = mid-1
        elif arr[mid]<key:
            low = mid+1
        else:
            low = mid
    if arr[low]!=key:
        return -1
    return low