    stones = n
    levels = []
    for i in range(n):
        levels.append(stones)
        if stones % 2 == 0:
            stones += 2
        else:
            stones += 2
    return levels


