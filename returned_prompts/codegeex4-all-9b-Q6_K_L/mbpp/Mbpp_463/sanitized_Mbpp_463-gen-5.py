def max_subarray_product(arr):
    max_product = 1
    min_product = 1
    result = 1
    for num in arr:
        if num == 0:
            max_product = min_product = 1
        else:
            temp = max_product
            max_product = max(num, max_product * num, min_product * num)
            min_product = min(num, min_product * num, temp * num)
            result = max(result, max_product)
    return result