
def find_solution(a: int, b: int, n: int) -> tuple:
    gcd = get_gcd(a, b)
    x = n // b
    y = n // a
    if x * b != n or y * a != n:
        return None
    return x, y

def get_gcd(a: int, b: int) -> int:
    if b == 0:
        return a
    else:
        return get_gcd(b, a % b)


