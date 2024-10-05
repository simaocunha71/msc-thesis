    words = txt.split()
    if not words:
        return len([c for c in txt if c.islower() and (ord(c) - ord('a')) % 2 == 1])
    return words


