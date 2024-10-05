    for ch in c:
        s = s.replace(ch, '')
    return (s, s == s[::-1])


