def start_withp(words):
    result = []
    for word in words:
        if word.startswith('p'):
            result.append(word.split()[0])
            if len(result) == 2:
                break
    return tuple(result) if len(result) == 2 else None