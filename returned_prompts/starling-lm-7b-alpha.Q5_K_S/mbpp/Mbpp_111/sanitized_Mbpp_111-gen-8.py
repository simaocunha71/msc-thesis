from collections import Counter
def common_in_nested_lists(lst):
    ctr = Counter()
    for sublist in lst:
        for elem in sublist:
            ctr.update(elem)
    return ctr.elements()