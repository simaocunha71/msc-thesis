def max_product(array):
    if not array:
        return 0

    n = len(array)
    max_product = [0] * n
    max_product[0] = array[0]

    for i in range(1, n):
        max_product[i] = array[i]
        for j in range(i):
            if array[i] > array[j]:
                max_product[i] = max(max_product[i], max_product[j] * array[i])

    return max(max_product)