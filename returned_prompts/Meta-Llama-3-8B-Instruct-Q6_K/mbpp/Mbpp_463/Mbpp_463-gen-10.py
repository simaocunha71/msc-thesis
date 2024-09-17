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



The function `max_subarray_product` takes an array as input and returns the maximum product of a subarray. It initializes `max_product`, `min_product`, and `result` with the first element of the array. Then, it iterates through the array, updating `max_product`, `min_product`, and `result` based on the current element and the previous maximum and minimum products.

If the current element is negative, it swaps `max_product` and `min_product` because a negative number can turn a maximum product into a minimum product and vice versa.

It keeps track of the maximum product seen so far and returns it at the end.

For example, for the input `[1, -2, -3, 0, 7, -8, -2]`, the function returns `112`, which is the maximum product of the subarray `[7, -8, -2]`.