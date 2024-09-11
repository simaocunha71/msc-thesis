from bisect import bisect_right as br

def find_kth(arr1, arr2, k):
    if len(arr1) < len(arr2):
        return find_kth(arr2, arr1, k)
    if k > len(arr1):
        return arr2[k - len(arr1) - 1]
    idx = br(arr2, arr1[k - 1])
    if idx == 0:
        return arr1[k - 1]
    elif idx == len(arr2):
        return arr2[len(arr2) - 1]
    else:
        if arr2[idx] < arr1[k - 1]:
            return find_kth(arr1, arr2[:idx + 1], k + (len(arr2) - idx))
        else:
            return find_kth(arr1[k:], arr2[:idx + 1], k)
```
    
However, this solution has an issue: if `arr1` is much larger than `arr2`, the time complexity of `find_kth` would be O(n^2). To solve this problem, we can use the binary search strategy and find the maximum index `idx` that satisfies `arr1[idx] < arr2[idx]`.

Here is a modified version of the function:

```python
def find_kth(arr1, arr2, k):
    if len(arr1) < len(arr2):
        return find_kth(arr2, arr1, k)
    if k > len(arr1):
        return arr2[k - len(arr1) - 1]
    if len(arr2) == 0:
        return arr1[k - 1]

    left = 0
    right = min(len(arr1), len(arr2))

    while left < right:
        mid = (left + right) // 2
        if arr1[mid] < arr2[mid]:
            left = mid + 1
        else:
            right = mid

    if left == 0:
        return arr1[k - 1]
    elif left