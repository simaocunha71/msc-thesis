

def fibfib(n: int):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b, c = 0, 0, 1
        for _ in range(n - 2):
            a, b, c = b, c, a + b + c
        return c


print(fibfib(1))
print(fibfib(5))
print(fibfib(8))


