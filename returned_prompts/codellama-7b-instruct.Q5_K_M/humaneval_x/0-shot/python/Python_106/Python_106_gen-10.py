
def f(n):
    def g(i):
        if i % 2 == 0:
            return i
        else:
            return sum(range(1, i + 1))
    return [g(i) for i in range(1, n + 1)]

