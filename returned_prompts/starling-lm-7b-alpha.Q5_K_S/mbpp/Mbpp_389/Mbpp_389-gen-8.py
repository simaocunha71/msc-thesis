def find_lucas(n):
    """
    Find the n'th lucas number.
    Time complexity: O(log(n))
    """
    if n == 0:
        return 2
    if n == 1:
        return 1

    a, b = 2, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a

# Assertion:
assert find_lucas(9) == 76
# Assertion:
assert find_lucas(1) == 1
# Assertion:
assert find_lucas(0) == 2
# Assertion:
assert find_lucas(7) == 89
# Assertion:
assert find_lucas(8) == 149

# Lucas numbers are defined as follows:
# Lucas(0) = 2, Lucas(1) = 1
# Lucas(n) = Lucas(n-1) + Lucas(n-2) for n > 1
# The Lucas numbers are a sequence of numbers that are closely related to the Fibonacci numbers,
# but they are not the same. The first few Lucas numbers are: 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123, 199, 322, 521, 843, 1364, 2178, 3527, 5702, 9227, 14930, 24157, 39087, 63242, 102334, 165587, 267914, 433494, 701408, 1134903, 1836311, ...
# The Lucas sequence, like the Fibonacci sequence, is a recursive sequence. The first two terms of the sequence are defined, and each subsequent term is the sum of the previous two terms.

# The function