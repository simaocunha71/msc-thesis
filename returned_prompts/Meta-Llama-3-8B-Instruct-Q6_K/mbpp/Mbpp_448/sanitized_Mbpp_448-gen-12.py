def perrin_sequence(n):
    if n <= 0:
        return
    yield 3
    yield 2
    a, b = 3, 2
    for _ in range(2, n):
        a, b = b, a + b
        yield b
def cal_sum(n):
    total = 0
    for _ in perrin_sequence(n):
        total += _
    return total