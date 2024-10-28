def find_kth(arr1, arr2, k):
    m, n = len(arr1), len(arr2)
    i, j = 0, 0
    while k > 0:
        if i == m:
            return arr2[j + k - 1]
        if j == n:
            return arr1[i + k - 1]
        if k == 1:
            return min(arr1[i], arr2[j])
        mid1 = min(i + k // 2, m)
        mid2 = min(j + k // 2, n)
        if arr1[mid1 - 1] < arr2[mid2 - 1]:
            k -= mid1 - i
            i = mid1
        else:
            k -= mid2 - j
            j = mid2
    return -1