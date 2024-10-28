```
def max_subarray_product(arr):
    if not arr:
        return 0
    max_product = arr[0]
    min_product = arr[0]
    result = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < 0:
            max_product, min_product = min_product, max_product
        max_product = max(arr[i], max_product * arr[i])
        min_product = min(arr[i], min_product * arr[i])
        result = max(result, max_product)
    return result
```




The problem is asking to find the maximum product subarray of the given array. The maximum product subarray is the contiguous subarray with the largest product.

The unit test `assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112` suggests that the maximum product subarray of the given array is 112. 

Here is a Python solution for the problem:

```
def max_subarray_product(arr):
    if not arr:
        return 0
    max_product = arr[0]
    min_product = arr[0]
    result = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < 0:
            max_product, min_product = min_product, max_product
        max_product = max(arr[i], max_product * arr[i])
        min_product = min(arr[i], min_product * arr[i])
        result = max(result, max_product)
    return result
```

This solution iterates over the array and for each element, it updates the maximum and minimum product of the subarray ending at the current element. It also keeps track of the maximum product seen so far. The maximum product subarray is the one with the maximum product. If the current element is negative, it swaps the maximum and minimum product because a negative number can change the maximum product to minimum product and vice versa.

The time complexity of this solution is O(n), where n is the length of the array, because it iterates over the array once. The space complexity is O(1), because it uses a constant amount of space to store the maximum and minimum product.