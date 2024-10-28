    result = []
    for idx in range(len(game)):
        result.append(abs(game[idx] - guess[idx]))
    return result


