    result = []
    for elem, guess in zip(game, guess):
        result.append(abs(elem - guess))

    return result


