
def next_Perfect_Square(n: int) -> int:
    n = n + 1
    while not is_Perfect_Square(n):
        n += 1
    return n

def is_Perfect_Square(n: int) -> bool:
    x = n**0.5
    return x == int(x)


