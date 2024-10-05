    result = []
    level_size = n
    while level_size > 0:
        result.append(level_size)
        if level_size % 2 == 0:
            level_size = level_size // 2
        else:
            level_size = (level_size // 2) + 1

    return result
