def find_solution(a, b, n):
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
            return (0, q)
        x = find_solution(b % a, a, r)
        if x is not None:
            y = (q - x[1]*b//a)
            return (x[0] + y*b//a, y)
        else:
            return None
    else:
        q, r = divmod(n, b)
        if r == 0:
            return (q, 0)
        x = find_solution(a % b, b, r)
        if x is not None:
            y = (q - x[0]*a//b)
            return (x[0], x[1] + y*a//b)
        else:
            return None