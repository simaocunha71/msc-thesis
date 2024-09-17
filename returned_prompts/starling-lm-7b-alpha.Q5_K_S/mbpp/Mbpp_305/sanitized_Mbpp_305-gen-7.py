def start_withp(words):
    pwords = []
    for word in words:
        if word[0] == 'p':
            pwords.append(word)
    if len(pwords) == 0:
        return None
    return pwords[0], pwords[1]