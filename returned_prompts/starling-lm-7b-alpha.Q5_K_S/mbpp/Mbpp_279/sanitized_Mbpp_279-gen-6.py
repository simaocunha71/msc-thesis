from math import sqrt
from typing import List
def is_num_decagonal(num: int) -> bool:
    if num < 0:
        return False
    if num == 0:
        return True
    if num == 1:
        return True
    if num == 2:
        return True
    if num == 3:
        return True
    if num == 4:
        return True
    if num == 5:
        return True
    if num == 6:
        return True
    if num == 7:
        return True
    if num == 8:
        return True
    if num == 9:
        return True
    if num == 10:
        return True
    if num % 2 != 0:
        return False
    if not is_num_decagonal(num // 2):
        return False
    return True