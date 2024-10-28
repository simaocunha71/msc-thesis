class EmptyArrayError(Exception):
    pass
def kth_element(arr, k):
    k -= 1
    if not arr:
        raise EmptyArrayError("The array is empty")
    if k < 0 or k >= len(arr):
        raise OutOfRangeError(f"k is out of range (1 <= k <= {len(arr)})")
    arr.sort()
    return arr[k]