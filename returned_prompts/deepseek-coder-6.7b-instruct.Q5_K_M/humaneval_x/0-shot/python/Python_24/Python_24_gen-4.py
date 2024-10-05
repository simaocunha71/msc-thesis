

def largest_divisor(n: int) -> int:
    for i in range(n-1, 0, -1):
        if n % i == 0:
            return i


print(largest_divisor(15))


# or use a more pythonic way:


def largest_divisor(n: int) -> int:
    return next(i for i in range(n-1, 0, -1) if n % i == 0)


print(largest_divisor(15))


# or with list comprehension:


def largest_divisor(n: int) -> int:
    return max([i for i in range(n-1, 0, -1) if n % i == 0])


print(largest_divisor(15))


# or using built-in functions:


def largest_divisor(n: int) -> int:
    return max((i for i in range(n-1, 0, -1) if n % i == 0))


print(largest_divisor(15))


# or with a single line:


def largest_divisor(n: int) -> int:
    return max((i for i in range(n-1, 1, -1) if n % i == 0), default=1)


print(largest_divisor(15))


# or with a single line and built-in function:


def largest_divisor(n: int) -> int:
    return max(i for i in range(n-1, 1, -1) if n % i == 0, default=1)


print(largest_divisor(15))


# or with a single line and built-in functions and reversed range:


def largest_divisor(n: int) -> int:
    return max(i for i in range(n//2, 1, -1) if n % i == 0, default=1)


print(largest_divisor(15))


# or with a single line