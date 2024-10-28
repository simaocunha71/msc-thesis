    result = []

    for idx, word in enumerate(s.split()):
        if len(word) == n:
            result.append(word)

    return result
