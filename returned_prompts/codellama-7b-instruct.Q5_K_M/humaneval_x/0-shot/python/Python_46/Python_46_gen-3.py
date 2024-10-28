
def fib4(n: int):
    if n <= 2:
        return 2*n-1
    else:
        return fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

