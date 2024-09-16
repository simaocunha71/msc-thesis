def merge_sorted_list(lst):
    return sorted(set(itertools.chain.from_iterable(lst)))