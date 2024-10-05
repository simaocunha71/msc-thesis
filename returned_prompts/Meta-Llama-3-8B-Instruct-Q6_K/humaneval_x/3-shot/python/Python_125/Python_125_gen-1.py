    words = txt.split()
    if not words:
        return sum(1 for i, c in enumerate(txt) if ord(c) - ord('a') % 2 == 0)

    return words


