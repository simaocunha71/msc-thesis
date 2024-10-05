    result = []

    for index, score in enumerate(game):
        if score == guess[index]:
            result.append(0)
        else:
            result.append(abs(score - guess[index]))

    return result


