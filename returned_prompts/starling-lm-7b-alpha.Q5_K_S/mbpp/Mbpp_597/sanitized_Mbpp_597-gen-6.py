from bisect import bisect_right as br
def find_kth(arr1, arr2, k):
    if len(arr1) < len(arr2):
        return find_kth(arr2, arr1, k)
    if k > len(arr1):
        return arr2[k - len(arr1) - 1]
    idx = br(arr2, arr1[k - 1])
    if idx == 0:
        return arr1[k - 1]
    elif idx == len(arr2):
        return arr2[len(arr2) - 1]
    else:
        if arr2[idx] < arr1[k - 1]:
            return find_kth(arr1, arr2[:idx + 1], k + (len(arr2) - idx))
        else:
            return find_kth(arr1[k:], arr2[:idx + 1], k)