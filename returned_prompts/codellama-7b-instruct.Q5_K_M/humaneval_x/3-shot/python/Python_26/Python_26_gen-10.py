    seen = set()
    unique = []
    for num in numbers:
        if num not in seen:
            unique.append(num)
            seen.add(num)

    return unique


