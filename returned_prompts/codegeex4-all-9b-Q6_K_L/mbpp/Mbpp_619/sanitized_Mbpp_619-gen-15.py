def move_num(s):
    alpha = ''
    num = ''
    for i in s:
        if i.isalpha():
            alpha += i
        else:
            num += i
    return alpha + num