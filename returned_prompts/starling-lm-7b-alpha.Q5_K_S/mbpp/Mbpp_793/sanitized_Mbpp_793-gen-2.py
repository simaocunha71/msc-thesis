def last(arr, x):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end)//2
        if arr[mid] == x:
            if mid == len(arr) - 1 or arr[mid + 1] != x:
                return mid
            else:
                start = mid + 1
        elif x > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return -1