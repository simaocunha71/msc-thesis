"""
def find_kth(arr1, arr2, k):
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if k == 1:
            return min(arr1[i], arr2[j])
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
        k -= 1
    if i == len(arr1):
        return arr2[j + k - 1]
    if j == len(arr2):
        return arr1[i + k - 1]
"""
