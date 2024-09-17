def capital_words_spaces(s):
    if s:
        return ' '.join(s[i] for i in range(len(s)) if i == 0 or s[i-1] == ' ' or s[i].islower())
    else:
        return ''