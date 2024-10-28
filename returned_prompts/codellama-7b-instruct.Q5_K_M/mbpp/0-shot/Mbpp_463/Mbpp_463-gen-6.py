```python
def max_subarray_product(arr):
    """
    :type arr: List[int]
    :rtype: int
    """
    if not arr:
        return 0

    max_product = arr[0]
    max_product_so_far = arr[0]
    min_product_so_far = arr[0]

    for i in range(1, len(arr)):
        max_product_so_far = max(arr[i], max_product_so_far * arr[i], min_product_so_far * arr[i])
        min_product_so_far = min(arr[i], max_product_so_far * arr[i], min_product_so_far * arr[i])
        max_product = max(max_product, max_product_so_far)

    return max_product
```
