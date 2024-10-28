def move_num(s):
    res = ''
    num = ''
    for char in s:
        if char.isdigit():
            num += char
        else:
            if num:
                res += num + char
                num = ''
            else:
                res += char
    if num:
        res += num
    return res