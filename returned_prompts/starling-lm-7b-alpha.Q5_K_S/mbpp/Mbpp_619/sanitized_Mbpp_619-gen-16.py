def move_num(str: str):
    return ''.join(filter(lambda x: not x.isdigit(), str)) + ''.join(filter(lambda x: x.isdigit(), str))