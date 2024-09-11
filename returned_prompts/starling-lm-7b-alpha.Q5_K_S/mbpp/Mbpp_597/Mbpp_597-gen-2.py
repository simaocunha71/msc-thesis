def find_kth(arr1, arr2, k):
    if k > len(arr1) + len(arr2):
        return None
    if k <= len(arr1):
        return arr1[k - 1]
    if k <= len(arr1) + len(arr2) // 2:
        return max(arr1[k - 1], arr2[k - len(arr1) - 1])
    return arr2[k - len(arr1) - len(arr2) - 1]

# Testing
print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5)) # 6
print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 6)) # 8
print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 10)) # 9
print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 11)) # None
print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 0)) # 1
print(find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 2)) # 2



def find_kth(arr1, arr2, k):
    if k > len(arr1) + len(arr2):
        return None
    if k <= len(arr1):
        return arr1[k - 1]
    if k <= len(arr1) + len(arr2) // 2:
        return max(arr1[k - 1], arr2[k - len(arr1) - 1])
    return arr2[k - len(arr1) - len(arr2) - 1]


# Testing