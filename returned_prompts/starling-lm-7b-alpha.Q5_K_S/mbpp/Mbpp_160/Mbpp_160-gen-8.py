
def find_solution(a, b, n):
    x = n
    y = 0
    while x % b != 0:
        x, y = x - (x % b), y + (x // b)
    if x == 0:
        return None
    return (y, x // b)


