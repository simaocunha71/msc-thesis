    words = txt.split()
    if not words:
        return sum(1 for i, c in enumerate(txt.lower()) if ord(c) % 2 == 1)
    else:
        return words


