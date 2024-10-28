    def collatz(n: int) -> List[int]:
        """ Collatz sequence generator, which is a generator that returns a sequence of integers. """
        while True:
            if n == 1:
                return
            if n % 2 == 0:
                yield n // 2
            else:
                yield 3 * n + 1
            n = next(i for i in collatz(n) if i % 2 == 0)

    result = list(collatz(n))
    return sorted(filter(lambda x: x % 2 == 1, result))


