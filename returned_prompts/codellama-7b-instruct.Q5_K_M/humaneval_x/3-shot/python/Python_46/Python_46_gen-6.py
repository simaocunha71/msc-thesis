    def fib4_recursive(n):
        if n == 0:
            return 0
        elif n == 1:
            return 0
        elif n == 2:
            return 2
        elif n == 3:
            return 0
        else:
            return fib4_recursive(n - 1) + fib4_recursive(n - 2) + fib4_recursive(n - 3) + fib4_recursive(n - 4)

    def fib4_iterative(n):
        if n == 0:
            return 0
        elif n == 1:
            return 0
        elif n == 2:
            return 2
        elif n == 3:
            return 0
        else:
            a, b, c = 0, 0, 0
            for _ in range(n - 4):
                a, b, c = b, c, a + b + c
            return a + b + c

    return fib4_iterative(n)


