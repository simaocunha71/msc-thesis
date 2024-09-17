def max_subarray_product(arr):
    max_product = arr[0]
    current_product = arr[0]
    for i in range(1, len(arr)):
        if current_product < 0:
            current_product = arr[i]
        else:
            current_product *= arr[i]
        if current_product > max_product:
            max_product = current_product
    return max_product