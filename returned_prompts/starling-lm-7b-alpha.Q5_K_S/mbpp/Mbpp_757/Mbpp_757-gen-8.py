
def count_reverse_pairs(str_list):
    return sum(i==i[::-1] for i in str_list)


