def move_num(s: str) -> str:
    num_str = ''
    for char in s:
        if char.isdigit():
            num_str += char
    return s.replace(num_str, '') + num_str