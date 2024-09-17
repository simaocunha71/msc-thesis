def find_solution(a: int, b: int, n: int) -> tuple:
    x = n * pow(b, 4, a * b)
    y = pow(x * a - n, 4, b * a)
    if x < 0 or y < 0:
        return None
    return (x, y)