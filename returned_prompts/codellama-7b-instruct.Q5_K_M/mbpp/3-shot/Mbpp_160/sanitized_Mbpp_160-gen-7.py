def find_solution(a: int, b: int, n: int) -> tuple:
    gcd = find_gcd(a, b)
    x = n // b
    y = n % b
    if x * b + y * a == n:
        return (x, y)
    else:
        return None