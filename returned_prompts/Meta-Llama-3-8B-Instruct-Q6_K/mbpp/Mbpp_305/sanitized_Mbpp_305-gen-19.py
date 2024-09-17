def start_withp(words):
    result = []
    for word in words:
        words = word.split()
        for w in words:
            if w.startswith('p'):
                result.append(w)
                if len(result) == 2:
                    return tuple(result)
    return ()