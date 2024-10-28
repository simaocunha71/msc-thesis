def start_withp(words):
    for word in words:
        if word.startswith('p'):
            return tuple(word.split())
    return None