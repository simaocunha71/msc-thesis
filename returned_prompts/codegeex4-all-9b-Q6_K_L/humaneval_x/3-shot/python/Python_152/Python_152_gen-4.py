    result = []
    for idx, elem in enumerate(game):
        result.append(abs(elem - guess[idx]))

    return result