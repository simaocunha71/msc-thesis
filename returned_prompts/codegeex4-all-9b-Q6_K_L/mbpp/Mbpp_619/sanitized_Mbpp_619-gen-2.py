def move_num(s):
    num = ''.join([i for i in s if i.isdigit()])
    alpha = ''.join([i for i in s if not i.isdigit()])
    return alpha + num