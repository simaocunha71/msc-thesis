
def fibfib(n):
    if n < 3:
        return 0
    a, b = 0, 1
    for _ in range(n-2):
        a, b = b, a+b
    return a

