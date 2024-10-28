    result = []
    for i, j in zip(game, guess):
        result.append(abs(i - j))
    return result

