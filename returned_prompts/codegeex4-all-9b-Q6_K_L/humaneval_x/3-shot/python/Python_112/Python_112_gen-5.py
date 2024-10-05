    s = s.lower()
    c = c.lower()

    for char in c:
        s = s.replace(char, '')

    if s == s[::-1]:
        return (s, True)
    else:
        return (s, False)

