    result = set()
    for c in string:
        if c.isalpha():
            result.add(c.lower())
    return len(result)


