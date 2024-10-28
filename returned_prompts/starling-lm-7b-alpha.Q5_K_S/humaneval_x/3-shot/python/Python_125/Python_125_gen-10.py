    words = []
    for c in txt:
        if c == ' ' or c == ',':
            words.append(txt[:txt.index(c)])
            txt = txt[txt.index(c):]
    if len(words) == 0:
        count = 0
        for c in txt:
            if ord(c) % 2 == 1:
                count += 1
        return count
    else:
        return words


