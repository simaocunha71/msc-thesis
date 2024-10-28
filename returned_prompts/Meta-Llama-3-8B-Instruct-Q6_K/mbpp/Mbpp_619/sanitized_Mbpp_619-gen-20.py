def move_num(s):
    result = ""
    num_str = ""
    for char in s:
        if char.isdigit():
            num_str += char
        else:
            if num_str:
                result += num_str
                num_str = ""
            result += char
    if num_str:
        result += num_str
    return result