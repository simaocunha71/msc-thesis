from collections import Counter
def frequency_lists(lst):
    return dict(Counter(sum(lst, [])))