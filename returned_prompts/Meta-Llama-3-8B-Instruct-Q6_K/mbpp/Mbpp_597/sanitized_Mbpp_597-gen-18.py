def find_kth(arr1, arr2, k):
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1
    x, y = len(arr1), len(arr2)
    start = 0
    while k > 0:
        if start >= x:
            return arr2[k-1]
        if k <= x:
            return arr1[k-1]
        k -= 1
        if arr1[start] <= arr2[0]:
            x -= 1
        else:
            y -= 1
            k -= 1
        start += 1
    return -1