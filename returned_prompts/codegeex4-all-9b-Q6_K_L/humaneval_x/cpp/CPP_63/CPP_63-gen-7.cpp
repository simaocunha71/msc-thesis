def fibfib(n):
    fib = [0, 0, 1]
    if n < 3:
        return fib[n]
    for i in range(3, n + 1):
        fib.append(fib[i - 1] + fib[i - 2] + fib[i - 3])
    return fib[n]

B:
def fibfib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

C:
def fibfib(n):
    if n < 3:
        return [0, 0, 1][n]
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

D:
def fibfib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

E:
def fibfib(n):
    if n < 3:
        return [0, 0, 1][n]
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

F:
def fibfib(n):
    if n < 3:
        return [0, 0, 1][n]
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

G:
def fibfib(n):
    if n < 3:
        return [0, 0, 1][n]
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

H:
def fibfib(n):
    if n < 3:
        return [0, 0, 1][n]
    else:
        return fibfib(n-1) + fibfib(n-2) + fibfib(n-3)

I:
def fibfib(n):
    if n < 3:
        return [0, 0, 1][n]
    else:
        return fibfib(n-1) + fibfib(n-2)