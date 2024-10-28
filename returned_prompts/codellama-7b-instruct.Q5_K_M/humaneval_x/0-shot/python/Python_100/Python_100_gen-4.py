
def make_a_pile(n):
    return [n] + make_a_pile(n + 1)
