
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    # your code goes here
    if n < 0:
        return []
    elif n == 0:
        return [1]
    else:
        res = []
        for i in range(n):
            if i % 2 == 0:
                res.append(f_even(i))
            else:
                res.append(f_odd(i))
        return res

def f_odd(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    return sum

def f_even(n):
    factorial = 1
    for i in range(n + 1):
        factorial *= i
    return factorial





# Run tests
assert f(5) == [1, 2, 6, 24, 120]
assert f(10) == [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
assert f(-1) == []
assert f(0) == [1]

print("All tests passed!")








































































```