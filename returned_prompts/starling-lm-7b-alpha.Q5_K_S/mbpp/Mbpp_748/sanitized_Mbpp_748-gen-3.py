def capital_words_spaces(s):
    res = ""
    for i in range(len(s)):
        if i == 0 or s[i-1] != " ":
            res += s[i]
        else:
            res += " " + s[i]
    return res