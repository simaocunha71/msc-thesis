def capital_words_spaces(s):
    if not s:
        return s
    if s[0].isupper():
        return s[0] + ' ' + capital_words_spaces(s[1:])
    else:
        return s[0] + capital_words_spaces(s[1:])