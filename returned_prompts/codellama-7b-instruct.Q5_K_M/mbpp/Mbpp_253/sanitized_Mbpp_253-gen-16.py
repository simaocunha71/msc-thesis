def count_integer(my_list: list) -> int:
    count = 0
    for i in my_list:
        if isinstance(i, int):
            count += 1
    return count