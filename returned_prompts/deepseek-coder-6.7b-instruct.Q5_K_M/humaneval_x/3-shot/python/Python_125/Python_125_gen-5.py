    words = txt.split(',')
    if len(words) == 1:
        words = txt.split()
        if len(words) == 1:
            return sum(1 for c in txt if c.islower() and (ord(c) - ord('a')) % 2 != 0)
    return words


