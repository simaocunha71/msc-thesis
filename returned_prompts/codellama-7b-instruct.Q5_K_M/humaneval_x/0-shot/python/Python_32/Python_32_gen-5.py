import math


def poly(xs: list, x: float):
    return sum([coeff * math.pow(x, i) for i, coeff in enumerate(xs)])


def find_zero(xs: list):
    if len(xs) % 2 == 1 or max(xs) == 0:
        return None
    else:
        return -xs[-1] / xs[-2]
