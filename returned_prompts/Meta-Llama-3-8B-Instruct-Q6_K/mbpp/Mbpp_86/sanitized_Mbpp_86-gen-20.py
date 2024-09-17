def centered_hexagonal_number(n):
    hexagonal_sum = 0
    hexagonal_num = 0
    centered_hexagonal_num = 0
    while True:
        hexagonal_sum += hexagonal_num
        centered_hexagonal_num += hexagonal_sum
        if n == 1:
            return centered_hexagonal_num
        hexagonal_num += 1
        n -= 1