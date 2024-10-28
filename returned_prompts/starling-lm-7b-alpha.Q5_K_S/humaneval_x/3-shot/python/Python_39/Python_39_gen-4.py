    fib_num = [0, 1, 1]
    fib = fib_num
    while True:
        fib_num.append(fib_num[-1] + fib_num[-2])
        if len(fib_num) > 2 and all(fib_num[-3] % i != 0 for i in fib):
            return fib_num[-1]


