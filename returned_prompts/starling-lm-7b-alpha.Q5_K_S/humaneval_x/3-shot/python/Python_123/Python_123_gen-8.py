    def collatz(n):
        result = []
        while n > 1:
            if n % 2 == 0:
                result.append(n)
                n = n // 2
            else:
                result.append(n)
                n = 3 * n + 1
        result.append(1)
        return result

    odds = filter(lambda x: x % 2 == 1, collatz(n))
    return sorted(odds)


