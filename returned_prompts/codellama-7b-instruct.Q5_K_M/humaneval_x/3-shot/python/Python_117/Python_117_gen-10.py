    words = []
    i = 0
    while i < len(s):
        word = ""
        while i < len(s) and s[i] != " ":
            word += s[i]
            i += 1
        if len(word) == n:
            words.append(word)
        i += 1
    return words


