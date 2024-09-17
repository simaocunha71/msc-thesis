
def find_solution(a: int, b: int, n: int) -> tuple:
    if a == 0 and b == 0:
        return None
    if a == 0:
        return (0, n)
    if b == 0:
        return (n, 0)
    d = hcf(a, b)
    a //= d
    b //= d
    if (n % d) != 0:
        return None
    n //= d
    if a == 1:
        return (n, 0)
    if b == 1:
        return (0, n)
    if n <= 0:
        return (None, None)
    x = b // a
    y = -a // b
    return (n * x, n * y)


