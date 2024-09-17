```
def find_kth(arr1, arr2, k):
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if i + j < k - 1:
            if arr1[i] < arr2[j]:
                i += 1
            else:
                j += 1
        else:
            if arr1[i] < arr2[j]:
                return arr1[i]
            else:
                return arr2[j]
    if i < len(arr1):
        return arr1[i]
    else:
        return arr2[j]
```
The function `find_kth` takes two sorted arrays `arr1` and `arr2` and an integer `k` as input. It returns the `kth` element from the combined array.

The function works by iterating over both arrays, comparing elements, and moving the pointer of the smaller element forward. When `k - 1` is reached, it compares the current elements of both arrays and returns the smaller one. If one array is exhausted before reaching `k - 1`, it returns the remaining element from the other array.

The unit test `assert find_kth([2, 3, 6, 7, 9], [1, 4, 8, 10], 5) == 6` ensures that the function returns the correct `kth` element. In this case, the `kth` element is the 6 at index 4 (0-indexed) in the combined array. The function correctly returns 6 as the result.