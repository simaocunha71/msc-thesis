

def fib4(n: int) -> int:
    fibs = [0, 0, 2, 0] + [0] * (n - 3)
    for i in range(4, n+1):
        fibs[i] = fibs[i-1] + fibs[i-2] + fibs[i-3] + fibs[i-4]
    return fibs[n]


if __name__ == "__main__":
    import doctest
    doctest.testmod()


In this function, we first initialize the first four elements of the list fibs with the four base cases of the fib4 sequence. Then we use a for loop to compute each subsequent element of the sequence by summing the previous four elements. The result is stored in the list fibs, which allows us to efficiently compute the n-th element in O(n) time. Finally, we return the n-th element of the fibs list.

The time complexity of this function is O(n), and the space complexity is also O(n) because we are storing all computed values in a list.
"""

#tests/test_fib4.py
from fib4 import fib4


def test_fib4():
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 4
    assert fib4(5) == 8
    assert fib4(6) == 14
    assert fib4(7) == 28
    assert fib4(8) == 54
    assert fib4(9) == 108
    assert fib4(10) == 228
    assert fib4(11) == 494
    assert fib4(12) == 1120
    assert fib4(13) == 2460
    assert fib4(14) == 5722
    assert fib4(15) == 13588
    assert fib4(16) == 31666
    assert fib4(17) == 77000
    assert fib