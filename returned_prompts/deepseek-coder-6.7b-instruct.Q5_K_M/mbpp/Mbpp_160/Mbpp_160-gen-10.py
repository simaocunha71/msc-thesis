
def find_solution(a, b, n):
    if a == 0 and b == 0:
        return None
    if a == 0:
        if n % b == 0:
            return (0, n // b)
        else:
            return None
    if b == 0:
        if n % a == 0:
            return (n // a, 0)
        else:
            return None
    if a > b:
        q, r = divmod(n, a)
        if r == 0:
            return (q, 0)
        x = find_solution(b, r, a % b)
        if x is None:
            return None
        return (q + x[0], x[1])
    if b > a:
        q, r = divmod(n, b)
        if r == 0:
            return (0, q)
        x = find_solution(a, r, b % a)
        if x is None:
            return None
        return (x[0], q + x[1])


