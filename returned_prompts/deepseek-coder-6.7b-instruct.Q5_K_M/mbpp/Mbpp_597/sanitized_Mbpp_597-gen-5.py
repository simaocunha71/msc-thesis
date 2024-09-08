def find_kth(arr1, arr2, k):
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1

    len1 = len(arr1)
    len2 = len(arr2)

    start = 0
    end = len1

    while start <= end:
        partition1 = (start + end) // 2
        partition2 = k - partition1

        l1 = arr1[partition1 - 1] if partition1 > 0 else float('-inf')
        l2 = arr2[partition2 - 1] if partition2 > 0 else float('-inf')
        r1 = arr1[partition1] if partition1 < len1 else float('inf')
        r2 = arr2[partition2] if partition2 < len2 else float('inf')

        if l1 > r2:
            end = partition1 - 1
        elif l2 > r1:
            start = partition1 + 1
        else:
            return max(l1, l2)

    return -1