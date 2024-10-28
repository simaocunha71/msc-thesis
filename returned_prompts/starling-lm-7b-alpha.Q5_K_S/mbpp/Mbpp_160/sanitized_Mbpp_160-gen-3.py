def find_solution(a, b, n):
    if a == 0 and b == 0 and n == 0:
        return (0, 0)
    elif a == 0 and b != 0 and n % b == 0:
        return (0, n // b)
    elif a != 0 and b == 0 and n % a == 0:
        return (n // a, 0)
    else:
        d = abs(b) - abs(a)
        if d == 0:
            return (None, None)
        if d < 0:
            return (None, None)
        else:
            x = (n - b) // a
            if a >= 0 and b >= 0:
                y = (n + b) // a
            elif a <= 0 and b <= 0:
                y = (n - b) // a
            elif a <= 0 and b >= 0:
                y = (n + b) // a
            elif a >= 0 and b <= 0:
                y = (n - b) // a
            return (x, y)