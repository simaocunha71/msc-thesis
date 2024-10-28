def start_withp(words):
    for word in words:
        if word.startswith('p') or word.startswith('P'):
            return tuple(word.split())