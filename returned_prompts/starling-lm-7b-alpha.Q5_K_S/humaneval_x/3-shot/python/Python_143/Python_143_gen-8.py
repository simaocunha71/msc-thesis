    words = sentence.split(' ')
    result = []
    for w in words:
        if all(w[i] == w[0] for i in range(1, len(w))):
            result.append(w)

    return ' '.join(result)


