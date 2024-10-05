    seen_chars = set()

    for char in string.lower():
        if char not in seen_chars:
            seen_chars.add(char)

    return len(seen_chars)


