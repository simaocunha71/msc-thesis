def find_kth(arr1, arr2, k):
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1
    x, y = len(arr1), len(arr2)
    for i in range(min(x, y), 0, -1):
        if x - i < 0:
            return arr2[k - 1]
        if y - i < 0:
            return arr1[k - 1]
        if arr1[x - i] > arr2[y - i]:
            return arr2[y - i]
        k -= i
    if k > 0:
        return arr2[k - 1]
    return arr1[k - 1]  # never reached