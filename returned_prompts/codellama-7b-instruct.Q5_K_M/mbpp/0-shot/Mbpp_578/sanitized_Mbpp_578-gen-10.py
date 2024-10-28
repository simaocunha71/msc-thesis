def interleave_lists(lists):
    return sum(map(list, zip(*lists)), [])