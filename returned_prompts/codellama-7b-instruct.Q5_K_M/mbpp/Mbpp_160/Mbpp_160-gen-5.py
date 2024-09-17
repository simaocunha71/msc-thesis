
def find_solution(a: int, b: int, n: int) -> tuple:
    if a * b == 0:
        return None
    x = n // b
    y = n // a
    if x * b == n:
        y -= 1
    if y * a == n:
        x -= 1
    return x, y


