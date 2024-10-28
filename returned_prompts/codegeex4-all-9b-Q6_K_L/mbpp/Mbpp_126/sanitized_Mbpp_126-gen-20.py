def sum(a: int, b: int) -> int:
    if a == b:
        return a
    if a > b:
        a, b = b, a
    divisors = [i for i in range(1, a+1) if a % i == 0 and b % i == 0]
    return sum(divisors)