def start_withp(words):
    result = []
    for word in words:
        if word.startswith('p'):
            result.append(word.split()[0])
    return tuple(result)