    fib_seq = [0, 1]
    for i in range(2, 10 ** 6):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        if fib_seq[-1] > 10 ** 6:
            break
        if all(fib_seq[-1] % i != 0 for i in range(2, int(fib_seq[-1] ** 0.5) + 1)):
            if fib_seq[-1] > n:
                return fib_seq[-2]
            else:
                return fib_seq[-1]
    return fib_seq[-1]


# Code for testing
if __name__ == "__main__":
    print(prime_fib(10 ** 6))


# End of Code


