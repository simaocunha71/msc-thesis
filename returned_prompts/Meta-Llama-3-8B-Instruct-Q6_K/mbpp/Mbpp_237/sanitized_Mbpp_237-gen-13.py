from collections import defaultdict
def check_occurences(lst):
    d = defaultdict(int)
    for item in lst:
        d[tuple(sorted(item))] += 1
    return dict(d)