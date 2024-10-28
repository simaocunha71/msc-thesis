"""
def right_insertion(sorted_list,val):
    right=len(sorted_list)
    left=0
    while left<right:
        mid=(left+right)//2
        if sorted_list[mid]>=val:
            right=mid
        else:
            left=mid+1
    return right
"""
