    words = txt.split()
    if len(words) == 1:
        words = txt.split(',')
    if len(words) == 1:
        count = sum(1 for c in txt if c.islower())
        return count % 2
    return words


