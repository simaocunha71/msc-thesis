def max_val(lst):
    lst_num = [i for i in lst if type(i) == int or type(i) == float]
    return max(lst_num)