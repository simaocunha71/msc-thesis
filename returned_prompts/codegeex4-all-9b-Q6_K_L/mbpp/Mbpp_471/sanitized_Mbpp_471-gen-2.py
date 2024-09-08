def find_remainder(arr, n):
    product = 1
    for num in arr:
        product = (product * num) % n
    return product