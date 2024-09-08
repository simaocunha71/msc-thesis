def move_num(s):
    num = [i for i in s if i.isdigit()]
    alpha = [i for i in s if not i.isdigit()]
    return ''.join(alpha + num)