def capital_words_spaces(s):
    result = ''
    for i in range(len(s)):
        if i > 0 and s[i-1].isupper():
            result += ' '
        result += s[i]
    return result