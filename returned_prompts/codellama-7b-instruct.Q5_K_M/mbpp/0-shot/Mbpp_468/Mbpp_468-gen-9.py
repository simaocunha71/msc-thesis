
def max_product(arr):
    n = len(arr)
    if n == 0:
        return 0
    max_product = arr[0]
    for i in range(1, n):
        if arr[i] > max_product:
            max_product = arr[i]
    for i in range(n - 2, -1, -1):
        if arr[i] > max_product:
            max_product = arr[i]
    return max_product









