def find_kth(arr1, arr2, k):
    if k > len(arr1) + len(arr2):
        return -1
    if len(arr1) == 0:
        return arr2[k - 1]
    if len(arr2) == 0:
        return arr1[k - 1]
    if k == 1:
        return min(arr1[0], arr2[0])

    mid1 = min(len(arr1), k // 2)
    mid2 = min(len(arr2), k // 2)

    if arr1[mid1 - 1] > arr2[mid2 - 1]:
        return find_kth(arr1, arr2[mid2:], k - mid2)
    else:
        return find_kth(arr1[mid1:], arr2, k - mid1)

assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6
"""
Explanation:
The merged array after sorting will look like this: [1, 2, 3, 4, 6, 7, 8, 9, 10]
So, the 5th element is 6.
"""



