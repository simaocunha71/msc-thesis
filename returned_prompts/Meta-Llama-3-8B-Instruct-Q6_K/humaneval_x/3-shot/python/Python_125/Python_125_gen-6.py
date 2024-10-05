    words = txt.split()
    if len(words) == 0:
        words = txt.split(',')
        if len(words) == 0:
            return sum(1 for i in range(len(txt)) if ord(txt[i]) % 2 != 0)
    return words


