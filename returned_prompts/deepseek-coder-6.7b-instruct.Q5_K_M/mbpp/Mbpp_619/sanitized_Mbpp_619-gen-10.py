def move_num(s):
    num_list = []
    str_list = []
    for i in s:
        if i.isnumeric():
            num_list.append(i)
        else:
            str_list.append(i)
    return ''.join(str_list + num_list)