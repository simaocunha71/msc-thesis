    levels = [n]

    while True:
        if n % 2 == 0:
            n = n + 1
        else:
            n = n + 2

        levels.append(n)

        if n == levels[0]:
            break

    return levels


