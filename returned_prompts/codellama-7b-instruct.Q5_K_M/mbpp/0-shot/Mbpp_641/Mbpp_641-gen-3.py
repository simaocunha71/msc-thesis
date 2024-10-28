def is_nonagonal(n):
    return n == sum(x**2 for x in range(1, int(n**0.5) + 1))

def nth_nonagonal(n):
    return sum(x**2 for x in range(1, n + 1))

for i in range(1, 101):
    assert is_nonagonal(i) == nth_nonagonal(i) == i


