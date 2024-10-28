def find_solution(a, b, n):
    if a == 0 and b == 0 and n == 0:
        return (0, 0)
    elif a == 0:
        return None
    elif b == 0:
        if n % a == 0:
            return (n // a, 0)
        else:
            return None
    else:
        if (n - 1) % b == 0:
            return (n - 1, n // b)
        else:
            return None