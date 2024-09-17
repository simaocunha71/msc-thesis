def find_kth(arr1, arr2, k):
    arr1 = iter(arr1)
    arr2 = iter(arr2)
    curr1 = next(arr1, None)
    curr2 = next(arr2, None)
    while curr1 is not None and curr2 is not None:
        if curr1 > curr2:
            k -= 1
            if k == 0:
                return curr1
            curr1 = next(arr1, None)
        else:
            k -= 1
            if k == 0:
                return curr2
            curr2 = next(arr2, None)
    if curr1 is None:
        return next(arr2, None)
    if curr2 is None:
        return next(arr1, None)

