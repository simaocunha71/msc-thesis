
def make_a_pile(n):
    if n == 0:
        return []
    elif n % 2 == 0:
        return [n] + make_a_pile(n+1)
    else:
        return [n] + make_a_pile(n+2)