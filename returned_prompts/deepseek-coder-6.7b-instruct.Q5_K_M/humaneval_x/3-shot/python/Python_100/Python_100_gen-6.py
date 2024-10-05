    levels = [n]
    for i in range(n):
        if n % 2 == 0:
            levels.append(levels[-1] + 2)
        else:
            levels.append(levels[-1] + 2)
    return levels[1:]


