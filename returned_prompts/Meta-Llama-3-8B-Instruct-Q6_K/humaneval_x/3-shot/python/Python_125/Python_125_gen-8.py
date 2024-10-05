    words = txt.split()
    if len(words) == 1:
        if ',' in txt:
            words = txt.split(',')
        else:
            return sum(1 for i in range(26) if txt[i].islower() and (i % 2 != 0))
    return words


