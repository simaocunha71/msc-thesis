def last(arr,element):
    start=0
    end=len(arr)-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==element:
            start=mid+1
        elif element>arr[mid]:
            start=mid+1
        else:
            end=mid-1
    if start==len(arr):
        return -1
    else:
        return start