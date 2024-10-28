def recursive_list_sum(l):
    flat_list = [item for sublist in l for item in sublist]
    return sum(flat_list)