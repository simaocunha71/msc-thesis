    lst_index = 0
    lst_sum = 0
    while lst_index < len(lst):
        if lst_index % 3 == 0 and lst_index % 4 != 0:
            lst_sum += lst[lst_index] ** 2
        elif lst_index % 4 == 0 and lst_index % 3 != 0:
            lst_sum += lst[lst_index] ** 3
        lst_index += 1
    return lst_sum