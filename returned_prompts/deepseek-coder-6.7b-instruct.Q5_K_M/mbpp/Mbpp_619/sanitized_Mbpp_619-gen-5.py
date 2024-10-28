def move_num(s):
    num_list = [i for i in s if i.isdigit()]
    str_list = [i for i in s if not i.isdigit()]
    return ''.join(str_list + num_list)