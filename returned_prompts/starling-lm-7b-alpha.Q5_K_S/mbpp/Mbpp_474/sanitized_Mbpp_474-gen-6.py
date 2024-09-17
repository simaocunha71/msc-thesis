def replace_char(string,char1,char2):
    new_str=""
    for c in string:
        if c==char1:
            new_str+=char2
        else:
            new_str+=c
    return new_str