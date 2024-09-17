def max_product(arr):
    max_product = [1] * len(arr)
    min_product = [1] * len(arr)
    result = arr[0]
    
    for i in range(1, len(arr)):
        max_product[i] = max(arr[i], max_product[i-1] * arr[i])
        min_product[i] = min(arr[i], min_product[i-1] * arr[i])
        result = max(result, max_product[i])
    
    return result