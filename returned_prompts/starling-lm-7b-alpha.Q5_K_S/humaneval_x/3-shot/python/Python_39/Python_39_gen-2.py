    fib_numbers = [0, 1]
    while True:
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])
        if is_prime(fib_numbers[-1]):
            return fib_numbers[-1]


