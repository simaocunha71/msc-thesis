    if n == 1:
        return 2
    if n == 2:
        return 3

    fib = [0, 1, 1]
    for i in range(3, n):
        fib.append(fib[i - 1] + fib[i - 2])

    for num in fib:
        if is_prime(num):
            return num


