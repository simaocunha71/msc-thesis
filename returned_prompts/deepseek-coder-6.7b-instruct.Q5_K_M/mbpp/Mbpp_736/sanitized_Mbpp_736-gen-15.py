import bisect
def left_insertion(arr, key):
    return bisect.bisect_left(arr, key)