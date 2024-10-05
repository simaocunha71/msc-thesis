    def collatz(n):
        if n % 2 == 0:
            yield from collatz(n//2)
            yield n//2
        else:
            yield from collatz(3*n+1)
            yield 3*n+1

    result = []
    for elem in collatz(n):
        if elem % 2 == 1:
            result.append(elem)

    return sorted(result)


