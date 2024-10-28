
def make_a_pile(n):
    pile = [n]
    for i in range(1, n):
        if n % 2 == 0:
            pile.append(n + 2 * i)
        else:
            pile.append(n + 2 * i)
    return pile

print(make_a_pile(3)) # [3, 5, 7]





