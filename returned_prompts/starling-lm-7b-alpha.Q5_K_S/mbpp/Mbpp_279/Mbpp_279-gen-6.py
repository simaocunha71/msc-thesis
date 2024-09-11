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


def num_decagonal(n: int) -> int:
    if n < 0:
        raise ValueError('n must be greater than 0')
    if not is_num_decagonal(n):
        raise ValueError('n must be a decagonal number')
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 4
    if n == 3:
        return 9
    if n == 4:
        return 16
    if n == 5:
        return 25
    if n == 6:
        return 36
    if n == 7:
        return 49
    if n == 8:
        return 64
    if n == 9:
        return 81
    if n == 10:
        return 100

    m = sqrt(1 + 8*n)
    return m * (2*n + 1)


def is_num_decagonal_list(nums: List[int]) -> List[bool]:
    return [is_num_decagonal(num) for num in nums]


def num_decagonal_list(nums