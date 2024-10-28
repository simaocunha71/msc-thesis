def find_solution(a: int, b: int, n: int) -> tuple:
    gcd = find_gcd(a, b)
    if gcd == 1:
        return None
    x = n // b
    y = n // a
    if x * b == n and y * a == n:
        return (x, y)
    return None