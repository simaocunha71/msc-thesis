    words = txt.split()
    if len(words) == 1 and ',' in txt:
        words = txt.split(',')
        if len(words) == 1:
            return sum(1 for c in txt if ord(c) % 2 == 1)
    return words


