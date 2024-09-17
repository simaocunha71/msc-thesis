def find_remainder(arr, n):
    product = 1
    for num in arr:
        product = (product % n) * (num % n) % n
    return product % n