def max_Product(arr):
    if len(arr) < 2:
        return (0,0)
    max_product = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            product = arr[i] * arr[j]
            if product > max_product:
                max_product = product
    return (arr[i], arr[j])