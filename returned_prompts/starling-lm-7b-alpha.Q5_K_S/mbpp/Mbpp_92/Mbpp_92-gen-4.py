
def is_undulating(n: int) -> bool:
    while n > 0:
        a = n % 10
        if a != 0 and a != 9:
            return False
        n = n // 10
    return True


