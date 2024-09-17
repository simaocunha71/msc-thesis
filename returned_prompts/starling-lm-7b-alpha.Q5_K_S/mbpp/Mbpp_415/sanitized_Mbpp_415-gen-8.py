def max_Product(arr):
    max_Product = (-99999999999999999999, -99999999999999999999)
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            max_Product = max(max_Product, (arr[i], arr[j]))
            max_Product = max(max_Product, (arr[j], arr[i]))
    return max_Product