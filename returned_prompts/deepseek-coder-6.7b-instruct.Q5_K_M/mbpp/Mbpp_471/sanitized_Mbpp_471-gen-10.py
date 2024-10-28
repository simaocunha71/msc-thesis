def find_remainder(lst, n):
    product = 1
    for i in lst:
        product = (product * i) % n
    return product