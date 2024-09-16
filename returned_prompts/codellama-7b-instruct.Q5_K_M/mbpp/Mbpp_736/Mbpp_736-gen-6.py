
"""
def left_insertion(arr,target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid=left+(right-left)//2
        if arr[mid]>=target:
            right=mid-1
        else:
            left=mid+1
    return left
"""