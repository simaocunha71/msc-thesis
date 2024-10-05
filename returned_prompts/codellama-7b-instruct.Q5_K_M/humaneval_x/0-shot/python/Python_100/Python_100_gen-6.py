
def make_a_pile(n):
    levels = []
    for i in range(n):
        levels.append(n)
        n = n + 1 if n % 2 else n + 2
    return levels[::-1]
