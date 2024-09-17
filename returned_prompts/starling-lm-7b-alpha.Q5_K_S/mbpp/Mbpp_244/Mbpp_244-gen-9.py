
def next_Perfect_Square(n):
    num = int(math.sqrt(n))
    while num ** 2 <= n:
        num += 1
    return num ** 2


