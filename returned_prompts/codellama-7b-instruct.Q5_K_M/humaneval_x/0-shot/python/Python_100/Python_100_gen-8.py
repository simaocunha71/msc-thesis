
def make_a_pile(n):
    pile = []
    while n > 0:
        pile.append(n)
        n = n % 2 + 1 if n % 2 else n + 1
    return pile
