def tuple_str_int(my_str) -> tuple:
    return tuple(map(int, my_str[1:-1].split(',')))