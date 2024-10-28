    result = []
    for word in text.split(' '):
        if word:
            result.append(word)
        else:
            result[-1] += '-'
    return '_'.join(result)


