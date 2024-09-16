def capital_words_spaces(string):
    result = ''
    i = 0
    while i < len(string):
        if string[i].isupper():
            result += string[i]
            i += 1
            while i < len(string) and string[i].islower():
                result += ' ' + string[i]
                i += 1
        else:
            result += string[i]
            i += 1
    return result