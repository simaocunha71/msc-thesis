def find_solution(a, b, n):
    def extended_euclidean(a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = extended_euclidean(b % a, a)
            return gcd, y - (b // a) * x, x

    gcd, x, _ = extended_euclidean(a, b)
    if n % gcd != 0:
        return None
    x0, _ = divmod(x * n // gcd, a)
    y0, _ = divmod(-x0 * b // gcd, b)
    return x0, y0