    pile = []
    current = 1
    for i in range(n):
        if i % 2 == 0:
            current += 1
        pile.append(current)
        current += 2 if i % 2 != 0 else 1
    return pile


