def tuple_str_int(tup_str: str) -> tuple:
    tup_str = tup_str.strip("()")
    num_list = tup_str.split(",")
    num_list = [int(num) for num in num_list]
    return tuple(num_list)