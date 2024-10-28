def insert_element(lst: list, elem: str) -> list:
    new_lst = [elem] * (2 * len(lst))
    new_lst[::2] = lst
    return new_lst