import bisect
def right_insertion(arr, x):
    return bisect.bisect_right(arr, x)