
def largest_divisor(n: int) -> int:
    divisor = 1
    while divisor < n:
        if n % divisor == 0:
            return divisor
        divisor += 1
    return 1
