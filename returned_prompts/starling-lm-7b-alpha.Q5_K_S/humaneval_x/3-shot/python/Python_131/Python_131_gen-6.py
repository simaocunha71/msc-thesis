    def helper(n):
        if not isinstance(n, int):
            raise TypeError("Input must be a positive integer")
        if n < 0:
            raise ValueError("Input must be a positive integer")
        if n == 0:
            return 0

        digits = []
        while n > 0:
            if n % 2 == 1:
                digits.append(n % 10)
            n = n // 10
        return reduce(lambda x, y: x * y, list(filter(lambda x: x % 2 != 0, digits)))

    return helper


