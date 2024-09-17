
def fib_lucas(a, b, n):
    if n == 0:
        return a
    if n == 1:
        return b
    else:
        return fib_lucas(b, a+b, n-1)
def find_lucas(n):
    return fib_lucas(1, 1, n)


