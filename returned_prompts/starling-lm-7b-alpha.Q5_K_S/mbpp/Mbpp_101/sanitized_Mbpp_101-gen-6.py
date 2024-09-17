from bisect import bisect_left as bl
def kth_element(arr, k):
    arr.sort()
    return arr[k-1]