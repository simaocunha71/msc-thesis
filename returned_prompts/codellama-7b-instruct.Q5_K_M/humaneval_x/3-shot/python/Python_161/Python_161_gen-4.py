    if s == s.lower():
        return s.upper()
    elif s == s.upper():
        return s.lower()
    else:
        return s[::-1]


