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


The idea is to keep track of the maximum and minimum product ending at each position. If the current element is negative, we swap the maximum and minimum product to account for the possibility of a negative product becoming positive. Then, we update the maximum product and minimum product by considering the current element and the product of the current element with the previous maximum and minimum product. Finally, we return the maximum product found.

The unit test `assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112` ensures that the function works correctly for the given array. The maximum product subarray for this array is [0, 7] with a product of 0 * 7 = 0, and the maximum product of the array is 112, which is the product of the maximum product subarray. The function returns the maximum product of the array, which is 112.