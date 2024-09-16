
from typing import List, Callable

def is_polite(n: int) -> bool:
    if not n:
        return False
    if str(n).count('0') >= 1:
        return False
    if str(n).count('5') >= 1:
        return False
    if str(n).count('9') >= 1:
        return False
    return True

def nth_polite_number(n: int, start_from: int = 1) -> int:
    if not n or not start_from:
        raise ValueError('n and start_from should be a positive integer')

    polite_numbers = []
    for i in range(start_from, 10**10):
        if is_polite(i):
            polite_numbers.append(i)
        if len(polite_numbers) == n:
            return polite_numbers[n - 1]

    return -1

tests = [
    (1, 11),
    (2, 22),
    (3, 33),
    (4, 44),
    (5, 55),
    (6, 66),
    (7, 77),
    (8, 88),
    (9, 99),
    (10, 111),
    (11, 122),
    (12, 133),
    (13, 144),
    (14, 155),
    (15, 166),
    (16, 177),
    (17, 188),
    (18, 199),
    (19, 211),
    (20, 222),
    (21, 233),
    (22, 244),
    (23, 255),
    (24, 266),
    (25, 277),
    (26, 288),
    (27, 299