import collections
def unique_sublists(L):
    res = collections.defaultdict(int)
    for sublist in map(tuple, L):
        res[sublist] += 1
    return res