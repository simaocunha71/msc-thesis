
    def largest_divisor(n: int) -> int:
        for i in range(n - 1, 0, -1):
            if n % i == 0:
                return i


if __name__ == "__main__":
    import doctest

    doctest.testmod()

#Problem_15/problem_15.py
