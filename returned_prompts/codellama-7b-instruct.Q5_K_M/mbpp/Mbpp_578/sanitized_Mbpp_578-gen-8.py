def interleave_lists(list_of_lists):
    return sum(zip(*list_of_lists), [])