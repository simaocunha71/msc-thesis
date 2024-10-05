

def sum_to_n(n: int):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


if __name__ == "__main__":
    import doctest

    doctest.testmod()

# 2. Write a Python function that calculates the factorial of a number.

