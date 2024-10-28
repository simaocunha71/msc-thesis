
def find_solution(a: int, b: int, n: int) -> tuple:
    gcd = 0
    x = 0
    y = 0

    if a == 0:
        if b == 0:
            if n == 0:
                return (0, 0)
            else:
                return None
        else:
            x = n
            y = 0
    elif b == 0:
        x = 0
        y = n
    else:
        gcd = _gcd(a, b)
        if n % gcd == 0:
            x = n // b
            y = a // b
        else:
            return None

    return (x, y)

def _gcd(a, b):
    while b != 0:
        t = b
        b = a % b
        a = t

    return a


