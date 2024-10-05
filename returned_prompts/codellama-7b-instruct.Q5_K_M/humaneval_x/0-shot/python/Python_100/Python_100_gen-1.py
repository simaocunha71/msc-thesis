
def make_a_pile(n):
    levels = []
    while n > 0:
        levels.append(n)
        n = (n + 1) if n % 2 == 0 else n + 1
    return levels
