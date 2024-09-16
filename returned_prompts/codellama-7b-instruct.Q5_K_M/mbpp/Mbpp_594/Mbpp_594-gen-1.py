
def diff_even_odd(my_list):
    if len(my_list) == 0:
        return None
    diff = my_list[1] - my_list[0]
    for i in range(2, len(my_list)):
        if my_list[i] - my_list[i-1] != diff:
            return None
    return diff
