"""
def left_insertion(mylist,target):
    left = 0
    right = len(mylist) - 1
    while left <= right:
        mid = (left + right) // 2
        if mylist[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    return left
"""
