
def max_product(arr):
    if len(arr) == 0:
        return 0
    max_product = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_product:
            max_product = arr[i]
        elif arr[i] * max_product < max_product:
            max_product = arr[i] * max_product
    return max_product


