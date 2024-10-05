
def fib4(n):
    a, b, c = 0, 0, 2
    for _ in range(n-1):
        d = a + b + c
        a = b
        b = c
        c = d
    return c

    # or

def fib4(n):
    a, b, c = 0, 0, 2
    for i in range(n-1):
        d = a + b + c
        a, b, c = b, c, d
    return c

    # or

def fib4(n):
    a, b, c = 0, 0, 2
    for i in range(n-1):
        a, b, c = b, c, a + b + c
    return c
