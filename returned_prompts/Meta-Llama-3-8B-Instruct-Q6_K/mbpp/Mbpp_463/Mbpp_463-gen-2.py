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


The function `max_subarray_product` takes a list of integers as input and returns the maximum product of a subarray. It initializes `max_product`, `min_product`, and `result` with the first element of the array. Then, it iterates over the array, updating `max_product`, `min_product`, and `result` accordingly. If an element is negative, it swaps `max_product` and `min_product`. The function finally returns `result`, which is the maximum product of a subarray. 

This function works correctly because the maximum product subarray can be either the subarray with the most positive numbers or the subarray with the most negative numbers (in which case the product would be maximized by including all negative numbers and one positive number). 

The unit test `assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112` helps to verify that the function works correctly. The maximum product subarray for this input is `[7, -8, -2]`, which has a product of `112`. 

Note that the function returns `0` if the input array is empty, which is a valid result according to the problem statement. 

The time complexity of this function is O(n), where n is the length of the input array, because it makes a single pass over the array. The space complexity is O(1), because it uses a constant amount of space to store the variables `max_product`, `min_product`, and `result`. 