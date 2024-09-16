def combinations_list(my_list):
    return _combinations_list(my_list, [])

def _combinations_list(my_list, comb_list):
    if not my_list:
        return [comb_list]
    else:
        comb_list.append(my_list[0])
        comb_list_a = _combinations_list(my_list[1:], comb_list)
        comb_list_b = _combinations_list(my_list[1:], comb_list[:])
        comb_list_b.append(comb_list)
        return comb_list_a + comb_list_b

