def is_majority(arr, n, x):
    # get the first and last occurences of x
    first = first_occurrence(arr, 0, n-1, x)
    if first == -1:
        return False
    last = last_occurrence(arr, 0, n-1, x)

    # if count of element is more than n/2, return True
    if last - first + 1 > n / 2:
        return True
    else:
        return False
def first_occurrence(arr, low, high, x):
    if high >= low:
        mid = (low + high) // 2
        if (mid == 0 or x > arr[mid - 1]) and arr[mid] == x:
            return mid
        elif x > arr[mid]:
            return first_occurrence(arr, mid + 1, high, x)
        else:
            return first_occurrence(arr, low, mid - 1, x)
    return -1
def last_occurrence(arr, low, high, x):
    if high >= low:
        mid = (low + high) // 2
        if (mid == high or x < arr[mid + 1]) and arr[mid] == x:
            return mid
        elif x < arr[mid]:
            return last_occurrence(arr, low, mid - 1, x)
        else:
            return last_occurrence(arr, mid + 1, high, x)
    return -1