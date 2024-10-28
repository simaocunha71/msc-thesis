    result = []
    for idx, elem in enumerate(guess):
        result.append(abs(game[idx] - elem))
    return result


