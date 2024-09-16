def find_kth(arr1, arr2, k):
    return min(arr1[-k], arr2[-k])

def find_kth(arr1, arr2, k):
    n1 = len(arr1)
    n2 = len(arr2)
    if n1 + n2 < k:
        raise ValueError
    if n1 + n2 == k:
        return min(arr1[-1], arr2[-1])
    if n1 + n2 > k:
        mid1 = n1 // 2
        mid2 = n2 // 2
        if find_kth(arr1[:mid1], arr2[:mid2], k):
            return find_kth(arr1[:mid1], arr2[:mid2], k)
        else:
            return find_kth(arr1[mid1:], arr2[mid2:], k - mid1 - mid2)

def find_kth(arr1, arr2, k):
    if k > len(arr1) + len(arr2):
        raise ValueError
    if k == len(arr1) + len(arr2):
        return min(arr1[-1], arr2[-1])
    if k > len(arr1):
        return arr2[-k]
    if k > len(arr2):
        return arr1[-k]
    if arr1[k - 1] < arr2[k - 1]:
        return arr1[k - 1]
    return arr2[k - 1]

def find_kth(arr1, arr2, k):
    if k > len(arr1) + len(arr2):
        raise ValueError
    if k == len(arr1) + len(arr2):
        return min(arr1[-1], arr2[-1])
    if k > len(arr1):
        return arr2[-k]
    if k > len(arr2):
        return arr1[-k]
    if arr1[k - 1] < arr2[k - 1]:
        return arr1[k - 1]
    return arr2[k - 1]

def find