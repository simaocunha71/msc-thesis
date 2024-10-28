
def capital_words_spaces(string):
    result = ''
    for i in range(len(string)):
        if string[i].isupper():
            result += ' ' + string[i]
        else:
            result += string[i]
    return result


