
def find_solution(a: int, b: int, n: int) -> tuple:
    if a == 0 and b == 0:
        return None
    elif a == 0:
        return (n, 0)
    elif b == 0:
        return (0, n)
    else:
        return (n / (b / a), n / (a / b))


