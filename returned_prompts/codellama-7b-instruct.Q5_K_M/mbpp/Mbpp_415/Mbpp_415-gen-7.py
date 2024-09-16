def max_Product(arr):
    if len(arr) == 0:
        return None
    max_product = 0
    max_i = 0
    max_j = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            product = arr[i] * arr[j]
            if product > max_product:
                max_product = product
                max_i = i
                max_j = j
    return arr[max_i], arr[max_j]
