def start_withp(words):
    for word in words:
        if word.split()[0][0] in ('P', 'p'):
            return tuple(word.split())