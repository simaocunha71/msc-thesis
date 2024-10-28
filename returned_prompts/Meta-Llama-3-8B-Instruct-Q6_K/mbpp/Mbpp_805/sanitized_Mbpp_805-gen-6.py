from itertools import chain, combinations
def max_sum_list(list_of_lists):
    max_sum = 0
    max_list = None
    for l in list_of_lists:
        if sum(l) > max_sum:
            max_sum = sum(l)
            max_list = l
    return max_list
list_of_lists = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]