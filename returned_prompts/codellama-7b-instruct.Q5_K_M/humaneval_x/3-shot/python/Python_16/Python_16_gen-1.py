    seen = set()
    for c in string.lower():
        if c not in seen:
            seen.add(c)

    return len(seen)


