def start_withp(words):
    result = []
    for word in words:
        if word.startswith('p'):
            result.append(word)
    if len(result) == 2:
        return result[0], result[1]
    elif len(result) == 1:
        return result[0], ''
    else:
        return '', ''