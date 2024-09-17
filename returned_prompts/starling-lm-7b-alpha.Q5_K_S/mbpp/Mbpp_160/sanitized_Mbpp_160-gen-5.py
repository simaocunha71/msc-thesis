def find_solution(a, b, n):
    if n % gcd(a, b) != 0:
        return None
    else:
        x, y = 0, 0
        while b:
            q = a // b
            r = a % b
            a, b = b, r
            x, y = y, x - q * y
        return (n / a, x)