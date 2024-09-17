def find_solution(a: int, b: int, n: int) -> tuple:
    if (a == 0 and b == 0) or (a == 0 and n % b == 0):
        return (0, n)
    if a == 0:
        return None
    if b == 0:
        return None
    if n % b != 0:
        return None
    d = hcf(a, b)
    x = (n / b) % d
    y = (n % a) / d
    return (x, y)
def hcf(a: int, b: int) -> int:
    if a < b:
        return hcf(b, a)
    if b == 0:
        return a
    return hcf(b, a % b)