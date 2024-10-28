def left_insertion(lst,num):
    l = 0
    r = len(lst)-1
    while l<r:
        mid = (l+r)//2
        if lst[mid]>=num:
            r = mid
        else:
            l = mid+1
    return l