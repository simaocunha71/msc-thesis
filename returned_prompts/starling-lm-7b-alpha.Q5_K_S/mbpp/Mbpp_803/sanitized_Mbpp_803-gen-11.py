import math
def is_perfect_square(n: int) -> bool:
    if n < 0:
        return False
    sq = int(n ** 0.5)
    return sq * sq == n