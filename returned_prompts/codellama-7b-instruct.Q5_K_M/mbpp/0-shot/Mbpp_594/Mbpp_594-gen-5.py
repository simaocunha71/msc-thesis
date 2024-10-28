def diff_even_odd(my_list):
    try:
        diff = my_list[1] - my_list[0]
    except IndexError:
        diff = 0
    return diff
