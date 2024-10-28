def move_num(s):
    s_list = list(s)
    num_list = [i for i in s_list if i.isdigit()]
    s_list = [i for i in s_list if not i.isdigit()]
    s_list.extend(num_list)
    return ''.join(s_list)