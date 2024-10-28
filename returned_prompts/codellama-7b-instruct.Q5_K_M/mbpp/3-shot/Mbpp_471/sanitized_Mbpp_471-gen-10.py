def find_remainder(arr: list, modulo: int) -> int:
    product = 1
    for i in arr:
        product = (product * i) % modulo
    return product