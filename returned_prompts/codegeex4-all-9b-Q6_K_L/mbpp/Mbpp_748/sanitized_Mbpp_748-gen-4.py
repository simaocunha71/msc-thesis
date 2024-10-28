def capital_words_spaces(s):
    result = ""
    for i in range(len(s)):
        if i == 0 or s[i] != s[i-1].lower():
            result += s[i]
        else:
            result += " " + s[i]
    return result