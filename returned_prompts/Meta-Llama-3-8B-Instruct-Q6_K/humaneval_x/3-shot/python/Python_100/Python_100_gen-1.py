    pile = [n]
    for i in range(1, n):
        if i % 2 == 0:
            pile.append(i * 2)
        else:
            pile.append(i * 2 + 1)
    return pile
