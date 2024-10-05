    def collatz(n):
        result = []
        while True:
            if n == 1:
                break
            if n % 2 == 0:
                result.append(n)
                n = n / 2
            else:
                result.append(n)
                n = 3 * n + 1
        result.append(1)
        return result

    result = []
    for elem in collatz(n):
        if elem % 2 != 0:
            result.append(elem)

    return result


