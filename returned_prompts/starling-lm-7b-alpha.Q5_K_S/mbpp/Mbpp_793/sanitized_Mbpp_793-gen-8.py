def last(a,x):
    n = len(a)
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] < x:
            left = mid + 1
        elif a[mid] > x:
            right = mid - 1
        else:
            if mid == n - 1 or a[mid + 1] < x:
                return mid
            else:
                right = mid - 1
    return left