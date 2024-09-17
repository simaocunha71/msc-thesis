from collections import defaultdict
from collections import Counter
def count_first_elements(tuples):
    d = defaultdict(int)
    for t in tuples:
        if isinstance(t, tuple):
            d[t[0]] += 1
        else:
            d[t] += 1
    return sum(d.values())