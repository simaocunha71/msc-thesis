def move_num(s):
    num_str = ''
    for char in s:
        if char.isdigit():
            num_str += char
        else:
            if num_str:
                s = s.replace(num_str, '', 1)
                s += num_str
                num_str = ''
    return s