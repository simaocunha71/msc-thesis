def hexagonal_num(n):
    triangular_num = (n * (n + 1)) // 2
    square_num = n * n
    hexagonal_num = 3 * triangular_num - square_num
    return hexagonal_num