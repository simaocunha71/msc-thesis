    def factorial(n):
        """ Implement the function factorial that takes n as a parameter,
        and returns the multiplication of the numbers from 1 to n.
        """
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(sum(range(1, i + 1)))

    return result


