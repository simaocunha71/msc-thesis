def interleave_lists(lists):
    return list(itertools.chain(*zip(*lists)))