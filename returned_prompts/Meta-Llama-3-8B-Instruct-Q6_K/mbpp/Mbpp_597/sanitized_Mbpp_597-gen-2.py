def find_kth(arr1, arr2, k):
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if k == 1:
            return min(arr1[i], arr2[j])
        k -= 1
        if arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    if i == len(arr1):
        return arr2[j - 1]
    else:
        return arr1[i - 1]  # k > 0 and k <= len(arr1) + len(arr2) - 1