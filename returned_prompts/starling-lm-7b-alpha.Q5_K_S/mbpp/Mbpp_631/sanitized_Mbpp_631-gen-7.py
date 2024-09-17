def replace_spaces(s):
    s_list = list(s)
    for i in range(len(s_list)):
        if s_list[i] == ' ':
            s_list[i] = '_'
    return ''.join(s_list)