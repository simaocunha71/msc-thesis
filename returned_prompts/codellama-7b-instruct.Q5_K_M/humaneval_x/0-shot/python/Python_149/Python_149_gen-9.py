
def sorted_list_sum(lst):
    return sorted(list(set([x for x in lst if len(x) % 2 == 0])))


