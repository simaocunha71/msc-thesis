def move_num(s):
    num_str = ''
    res = ''
    for char in s:
        if char.isdigit():
            num_str += char
        else:
            if num_str:
                res += num_str
                num_str = ''
            res += char
    if num_str:
        res += num_str
    return res