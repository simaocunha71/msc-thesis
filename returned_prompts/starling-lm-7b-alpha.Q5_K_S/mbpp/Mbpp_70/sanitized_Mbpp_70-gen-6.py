def get_equal(tuples_list):
    len_list = []
    for i in range(len(tuples_list)):
        len_list.append(len(tuples_list[i]))
    if len(set(len_list)) == 1:
        return True
    else:
        return False