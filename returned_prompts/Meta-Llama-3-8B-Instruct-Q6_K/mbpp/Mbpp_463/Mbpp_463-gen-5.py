```
def max_subarray_product(arr):
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


The function `max_subarray_product` takes a list of integers as input and returns the maximum product of a subarray. It initializes three variables: `max_product`, `min_product`, and `result` with the first element of the array. Then, it iterates over the array, updating `max_product` and `min_product` based on whether the current element is positive or negative. If the current element is negative, it swaps `max_product` and `min_product` to account for the possibility of a negative product. Finally, it updates `result` with the maximum of `result` and `max_product`. The function returns `result` as the maximum product of a subarray.

The unit test `assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112` ensures that the function correctly finds the maximum product subarray in the given array. The expected output is 112, which is the maximum product of the subarray `[1, 0, 7]`. The function correctly identifies this subarray as the maximum product subarray and returns the correct result.