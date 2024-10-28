def max_product(arr):
    n = len(arr)
    max_product = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[i] > arr[j]:
                max_product[i] = max(max_product[i], max_product[j] * arr[i])
    return max(max_product)