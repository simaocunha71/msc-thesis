def max_product(arr):
    n = len(arr)
    max_prod = 1
    for i in range(n):
        for j in range(i, n):
            prod = 1
            for k in range(i, j + 1):
                prod *= arr[k]
            max_prod = max(max_prod, prod)
    return max_prod