    words = txt.split()
    if not words:
        return sum(1 for i, c in enumerate(txt) if 'a' <= c <= 'z' and i % 2 != 0)

    return words


