    result = []
    for idx, elem in enumerate(guess):
        if elem == game[idx]:
            result.append(0)
        else:
            result.append(abs(game[idx] - elem))
    return result


