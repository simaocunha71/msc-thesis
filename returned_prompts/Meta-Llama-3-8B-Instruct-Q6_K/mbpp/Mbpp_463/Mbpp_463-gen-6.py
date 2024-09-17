The problem is asking for a function that finds the maximum product subarray of a given array. This means we need to find the product of a subarray that has the maximum product among all possible subarrays.

The unit test `assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112` suggests that the function should return the maximum product of a subarray, not the subarray itself.

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

In this function, we initialize three variables: `max_product`, `min_product`, and `result`. `max_product` and `min_product` are used to keep track of the maximum and minimum product ending at the current position, respectively. `result` is used to store the maximum product found so far.

We then iterate through the array. If the current element is negative, we swap `max_product` and `min_product` because a negative number can turn the maximum product into the minimum product and vice versa.

We then update `max_product` and `min_product` by taking the maximum and minimum of the current element and the product of the current element and the previous `max_product` or `min_product`.

Finally, we update `result` by taking the maximum of `result` and `max_product`. At the end of the function, `result` will be the maximum product subarray.  If the array is empty, the function returns 0.  If the array is not empty, it returns the maximum product.  This function should pass the given unit test. 