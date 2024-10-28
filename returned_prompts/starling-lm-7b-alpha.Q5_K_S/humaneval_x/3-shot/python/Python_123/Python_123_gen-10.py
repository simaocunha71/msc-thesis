    result = []

    def collatz(n):
        if n % 2 == 0:
            return n / 2
        else:
            return 3 * n + 1

    def odd_collatz(n):
        if n == 1:
            return [1]
        elif n % 2 == 0:
            return odd_collatz(n / 2) + [n / 2]
        else:
            return odd_collatz(collatz(n)) + [collatz(n)]

    result = odd_collatz(n)
    result.sort()

    return result


