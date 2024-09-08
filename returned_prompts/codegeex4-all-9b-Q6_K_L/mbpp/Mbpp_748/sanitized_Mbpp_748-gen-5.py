def capital_words_spaces(s: str) -> str:
    s = list(s)
    for i in range(1, len(s)):
        if s[i].isupper() and s[i-1].islower():
            s.insert(i, ' ')
    return ''.join(s)