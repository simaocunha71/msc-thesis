def find_remainder(lst, n):
    prod = 1
    for num in lst:
        prod = (prod * num) % n
    return prod