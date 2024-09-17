def find_solution(a, b, n):
    if (b == 0):
        if (n % a == 0):
            return (n//a, 0)
        else:
            return None
    else:
        y = (n - (a % b)) // b
        x = (n - b * y) // a
        return (x, y)