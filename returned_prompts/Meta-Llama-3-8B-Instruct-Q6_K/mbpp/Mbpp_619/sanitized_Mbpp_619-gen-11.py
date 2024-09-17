def move_num(s):
    num_str = ''
    result = ''
    for char in s:
        if char.isdigit():
            num_str += char
        else:
            result += char
    return result + num_str