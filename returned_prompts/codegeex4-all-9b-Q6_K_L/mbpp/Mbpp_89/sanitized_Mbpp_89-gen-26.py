def closest_num(n: int) -> int:
    while n > 0:
        if n - 1 == 0:
            return 0
        elif n - 1 % 2 == 1:
            return n - 1
        n -= 1