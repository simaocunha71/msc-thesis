import collections
def unique_sublists(my_list):
    return collections.Counter(map(tuple, my_list))