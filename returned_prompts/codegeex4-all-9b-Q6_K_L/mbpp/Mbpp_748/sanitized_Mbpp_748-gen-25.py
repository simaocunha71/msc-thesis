def capital_words_spaces(s):
    result = ""
    for i in range(len(s)):
        if i > 0 and s[i].isupper() and s[i-1].islower():
            result += " "
        result += s[i]
    return result