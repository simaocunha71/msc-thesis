def replace_spaces(string):
    res = []
    for c in string:
        if c == ' ':
            res.append('_')
        else:
            res.append(c)
    return ''.join(res)