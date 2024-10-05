    result = []
    for score, guess in zip(game,guess):
        result.append(abs(score - guess))
    return result


