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


The function takes an array of integers as input and returns the maximum product of a subarray. It initializes the maximum product, minimum product, and result as the first element of the array. Then, it iterates over the array, updating the maximum product and minimum product based on whether the current element is positive or negative. The result is updated as the maximum of the current result and the maximum product. The function finally returns the result. The unit test `assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112` ensures that the function works correctly.