def capital_words_spaces(string):
    i, j = 0, 0
    while j < len(string):
        if string[j].isupper():
            if i != j:
                string = string[:i] + ' ' + string[i:j] + ' ' + string[j]
                j += 1
            i = j
        else:
            j += 1
    if i != j:
        string = string[:i] + ' ' + string[i:]
    return string