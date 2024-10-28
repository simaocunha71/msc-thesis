def find_kth(arr1, arr2, k):
    i, j = 0, 0
    while True:
        if i == len(arr1):
            return arr2[j + k - 1]
        if j == len(arr2):
            return arr1[i + k - 1]
        if k == 1:
            return min(arr1[i], arr2[j])

        new_i = min(i + k // 2 - 1, len(arr1) - 1)
        new_j = min(j + k // 2 - 1, len(arr2) - 1)
        pivot1, pivot2 = arr1[new_i], arr2[new_j]
        if pivot1 <= pivot2:
            k -= new_i - i + 1
            i = new_i + 1
        else:
            k -= new_j - j + 1
            j = new_j + 1

