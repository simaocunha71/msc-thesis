    def fib4(n):
        fib_sequence = [0, 0, 2, 0, 4]
        while len(fib_sequence) <= n:
            fib_sequence.append(fib_sequence[-1] + fib_sequence[-2] + fib_sequence[-3] + fib_sequence[-4])
        return fib_sequence[n]


