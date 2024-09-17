def capital_words_spaces(s):
    res = ""
    for c in s:
        if c.isupper():
            res += " " + c
        else:
            res += c
    return res