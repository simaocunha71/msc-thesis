"""
def left_insertion(lst,val):
    left=0
    right=len(lst)
    while left<right:
        mid=left+(right-left)//2
        if lst[mid]>=val:
            right=mid
        else:
            left=mid+1
    return left
"""
