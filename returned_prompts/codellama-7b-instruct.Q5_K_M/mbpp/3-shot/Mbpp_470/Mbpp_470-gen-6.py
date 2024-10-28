
def add_pairwise(num_tup):
    num_list = list(num_tup)
    for i in range(len(num_list)-1):
        num_list[i] += num_list[i+1]
    return tuple(num_list)


