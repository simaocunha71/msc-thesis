def consecutive_duplicates(my_list: list) -> list:
    new_list = []
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
    return new_list