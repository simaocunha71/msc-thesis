def closest_num(n: int) -> int:
    if n <= 10:
        return n - 1
    else:
        return n - 1 if n % 10 == 0 else n - n % 10