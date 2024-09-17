def find_solution(a: int, b: int, n: int) -> tuple:
    if a * b < 0:
        if n % 2 != 0:
            return None
        else:
            return (n//b, -n//a)
    else:
        if n % (a + b) != 0:
            return None
        else:
            x = (n//(a + b)) * a
            y = (n//(a + b)) * b
            return (x, y)