def last(arr,val):
    start = 0
    end = len(arr)-1
    while(start<=end):
        mid = (start+end)//2
        if(arr[mid] == val):
            if(mid == len(arr)-1):
                return mid
            else:
                if(arr[mid+1]!=val):
                    return mid
                else:
                    start = mid+1
        elif(arr[mid] > val):
            end = mid - 1
        else:
            start = mid + 1
    return -1