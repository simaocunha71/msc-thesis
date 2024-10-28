def remove_odd(lst: list) -> list:
    new_list = [i for i in lst if i % 2 == 0]
    return new_list