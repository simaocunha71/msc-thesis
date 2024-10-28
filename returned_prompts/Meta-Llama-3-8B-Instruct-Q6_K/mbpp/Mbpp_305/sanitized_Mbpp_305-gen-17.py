def start_withp(words):
    result = []
    for word in words:
        for w in word.split():
            if w.startswith('p'):
                result.append(w)
    return tuple(result)