
def f(n):
    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            result.append(i)
        else:
            result.append(sum(range(1, i + 1)))
    return result

# Tests
assert f(5) == [1, 2, 6, 24, 15]
assert f(4) == [1, 2, 6, 24]
assert f(3) == [1, 2, 6]
assert f(2) == [1, 2]


def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """

    def factorial(n):
        """ the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i)."""
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

# Tests
assert f(5) == [1, 2, 6, 24, 15]
assert f(4) == [1, 2, 6, 24]
assert f(3) == [1, 2, 6]
assert f(2) == [1, 2]


def f(n):
    """ Implement the function f that takes n