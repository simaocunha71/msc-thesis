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

This function iterates over the array, keeping track of the maximum and minimum product ending at each position. When the product becomes negative, we swap the maximum and minimum product to handle the case when the product becomes positive again. The maximum product found is returned as the result. 

The unit test `assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112` checks if the function correctly finds the maximum product subarray in the given array. 

Note: The time complexity of this function is O(n), where n is the length of the input array, as it iterates over the array once. The space complexity is O(1), as it uses a constant amount of space to store the maximum and minimum product. 





