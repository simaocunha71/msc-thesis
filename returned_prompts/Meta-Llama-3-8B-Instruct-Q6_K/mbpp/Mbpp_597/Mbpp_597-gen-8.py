```
def find_kth(arr1, arr2, k):
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1
    x, y = len(arr1), len(arr2)
    start = 0
    while k > 0:
        if start >= x:
            return arr2[k-1]
        if k <= x:
            return arr1[k-1]
        k -= 1
        if arr1[start] <= arr2[0]:
            x -= 1
        else:
            y -= 1
            k -= 1
        start += 1
    return -1
```

The function `find_kth(arr1, arr2, k)` takes as input two sorted arrays `arr1` and `arr2`, and an integer `k`. It returns the `kth` element from the merged array. The function assumes that the arrays are sorted in ascending order. If `k` is greater than the sum of the lengths of the arrays, the function returns the last element of the merged array. If `k` is less than or equal to the length of the first array, the function returns the `kth` element of the first array. Otherwise, the function returns the `kth` element of the merged array.

The function uses a two-pointer technique to find the `kth` element. It initializes two pointers, `start`, to the beginning of the first array, and `x` and `y` to the lengths of the first and second arrays, respectively. It then enters a loop that continues until `k` becomes zero.

In each iteration of the loop, the function checks if `start` is greater than or equal to `x`, which means that the `kth` element is in the second array. If this is the case, the function returns the `kth` element of the second array.

If `k` is less than or equal to `x`, the function returns the `kth` element of the first array.

Otherwise, the function decrements `k` by one and checks if the element at index `start` in the first array is less than or equal to the element at index 0 in the second array. If this is the case, the function decrements `x` by one and increments `start` by one. Otherwise, the function decrements `y` by one and decrements `k` by