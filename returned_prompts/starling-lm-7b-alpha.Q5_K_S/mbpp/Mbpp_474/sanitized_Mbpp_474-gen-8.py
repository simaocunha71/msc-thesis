def replace_char(string,char,replace):
    res = ""
    for c in string:
        if c == char:
            res += replace
        else:
            res += c
    return res