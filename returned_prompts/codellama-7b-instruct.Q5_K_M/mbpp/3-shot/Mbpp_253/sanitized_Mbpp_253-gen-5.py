def count_integer(my_list: list) -> int:
    return len([i for i in my_list if isinstance(i, int)])