def find_remainder(arr, n):
    product = 1
    for num in arr:
        product *= num % n
    return product % n