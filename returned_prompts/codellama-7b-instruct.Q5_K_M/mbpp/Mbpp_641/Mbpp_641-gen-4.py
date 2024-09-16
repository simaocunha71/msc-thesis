def is_nonagonal(n):
    x = 2**(n-1)
    return x * (x + 1) * (2 * x + 1) // 6

def test(n):
    assert is_nonagonal(n) == nth_nonagonal_number(n)


def nth_nonagonal_number(n):
    return sum(range(1, n + 1))**2
