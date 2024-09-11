def move_num(s):
    num_str = ''
    result = ''
    for char in s:
        if char.isdigit():
            num_str += char
        else:
            result += char
            if num_str:
                result += num_str
                num_str = ''
    return result + num_str