    def collatz(n):
        result = []
        while n != 1:
            if n % 2 == 0:
                result.append(n)
                n = n / 2
            else:
                result.append(n)
                n = 3 * n + 1
        result.append(n)
        return result

    result = []
    for i in range(1, n + 1):
        if i % 2 != 0:
            result.extend(collatz(i))
    result.sort()
    return result


