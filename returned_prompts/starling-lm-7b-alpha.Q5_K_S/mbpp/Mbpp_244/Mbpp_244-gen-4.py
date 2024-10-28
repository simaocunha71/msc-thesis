
import math
def next_Perfect_Square(num):
    if num < 0:
        return -1
    square_root = int(math.sqrt(num))
    if square_root * square_root == num:
        return square_root * square_root
    else:
        return (square_root + 1) * (square_root + 1)


