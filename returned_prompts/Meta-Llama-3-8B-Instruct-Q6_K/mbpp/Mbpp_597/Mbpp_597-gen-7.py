```
def find_kth(arr1, arr2, k):
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if k == 1:
            return min(arr1[i], arr2[j])
        k -= 1
        if arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    if i < len(arr1):
        return arr1[i]
    return arr2[j]
```





This function works by maintaining two pointers, one for each array, and moving them through the arrays based on the value of the current element. If the current element in `arr1` is smaller, the pointer for `arr1` moves forward. If the current element in `arr2` is smaller, the pointer for `arr2` moves forward. This process continues until the `kth` element is found or one of the arrays is exhausted. If one of the arrays is exhausted, the function returns the `kth` element from the other array. The time complexity of this function is O(m + n), where `m` and `n` are the lengths of the input arrays. The space complexity is O(1), as it only uses a constant amount of space.