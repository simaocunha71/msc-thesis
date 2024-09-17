def move_num(s):
    n_list = []
    for i in s:
        if i.isdigit():
            n_list.append(i)
    for i in n_list:
        s = s.replace(i, '')
    return s + "".join(n_list)