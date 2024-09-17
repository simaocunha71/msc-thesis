from collections import Counter
def find_tuples(l, k):
    res = []
    for t in l:
        if all(i % k == 0 for i in t):
            res.append(t)
    return res