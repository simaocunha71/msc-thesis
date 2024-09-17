def is_perfect_square(n: int) -> bool:
    sqrt_n = int(n ** 0.5)
    return sqrt_n * sqrt_n == n