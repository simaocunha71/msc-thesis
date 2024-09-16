def pair_xor_Sum(my_list, num):
    return sum([x^y for x,y in zip(my_list,my_list[1:])])