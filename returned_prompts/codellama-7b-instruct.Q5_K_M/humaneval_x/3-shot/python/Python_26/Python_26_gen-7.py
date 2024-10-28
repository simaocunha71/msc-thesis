    seen = set()
    unique = []

    for n in numbers:
        if n not in seen:
            unique.append(n)
            seen.add(n)

    return unique


