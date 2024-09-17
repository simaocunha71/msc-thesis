
def find_solution(a, b, n):
    # Extended Euclidean Algorithm
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, x, y = egcd(b % a, a)
            return (g, y - (b // a) * x, x)

    gcd, x, y = egcd(a, b)

    if n % gcd != 0:
        return None

    return (x * n // gcd, y * n // gcd)


