    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    fib4 = [0, 0, 2, 0]

    for i in range(4, n + 1):
        fib4.append(fib4[i - 1] + fib4[i - 2] + fib4[i - 3] + fib4[i - 4])

    return fib4[n]