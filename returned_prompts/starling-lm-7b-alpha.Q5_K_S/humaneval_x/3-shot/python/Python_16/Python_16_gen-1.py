    distinct_characters = set()
    for c in string:
        if c.isalpha():
            distinct_characters.add(c.lower())
    return len(distinct_characters)


