def max_product(arr):
    max_product = [0] * len(arr)
    min_product = [0] * len(arr)
    max_product[0] = arr[0]
    min_product[0] = arr[0]
    
    for i in range(1, len(arr)):
        max_product[i] = max(arr[i], max_product[i-1] * arr[i], min_product[i-1] * arr[i])
        min_product[i] = min(arr[i], max_product[i-1] * arr[i], min_product[i-1] * arr[i])
    
    return max(max_product)