def last_Digit(n: int) -> int:
    while n >= 10:
        n = n//10
    return n