import math
def find_star_num(n):
    square = 1
    while True:
        if (math.sqrt(square) % 1 == 0):
            if n == 1:
                return square - 1
            n -= 1
        square += 1