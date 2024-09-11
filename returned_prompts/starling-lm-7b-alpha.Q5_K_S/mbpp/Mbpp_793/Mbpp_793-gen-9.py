def last(arr,val):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = start + (end - start)//2
        if arr[mid] == val:
            if mid == len(arr) - 1:
                return mid
            if arr[mid+1] != val:
                return mid
            else:
                start = mid + 1
        elif arr[mid] < val:
            start = mid + 1
        else:
            end = mid - 1
    return -1


# assert last([1,2,3],1) == 0

"""
def last(arr,val):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = start + (end - start)//2
        if arr[mid] == val:
            if mid == len(arr) - 1:
                return mid
            if arr[mid+1] != val:
                return mid
            else:
                start = mid + 1
        elif arr[mid] < val:
            start = mid + 1
        else:
            end = mid - 1
    return -1
"""

def test_last():
    assert last([1,2,3],1) == 0
    assert last([1,2,3],2) == 1
    assert last([1,2,3],3) == 2
    assert last([1,2,3],4) == -1
    assert last([1,2,3],0) == -1

test_last()

"""
def last(arr,val):
    if not arr:
        return -1
    if arr[-1] == val:
        return len(arr) - 1
    elif arr[-1] < val:
        return last(arr[:-1],val)
    else:
        return last(arr[:-1],val)
"""

"""
def last(arr,val):
    for i in range(len(arr)-1,-1,-1):
        if arr[i] == val:
