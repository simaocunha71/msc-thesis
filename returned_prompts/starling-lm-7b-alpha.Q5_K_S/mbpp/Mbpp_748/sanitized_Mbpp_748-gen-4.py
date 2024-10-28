def capital_words_spaces(string):
    """
    Input: string
    Output: string
    """
    result = []
    for i in range(len(string)):
        if i == 0:
            result.append(string[i])
        elif string[i-1] == ' ' and string[i] >= 'A' and string[i] <= 'Z':
            result.append(' ')
            result.append(string[i])
        else:
            result.append(string[i])
    return ''.join(result)