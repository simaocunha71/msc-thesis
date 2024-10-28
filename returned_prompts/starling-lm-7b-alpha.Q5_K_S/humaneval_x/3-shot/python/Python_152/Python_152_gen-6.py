    result = []
    for i in range(len(game)):
        diff = abs(game[i] - guess[i])
        result.append(diff)
    return result


