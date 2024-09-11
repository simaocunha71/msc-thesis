from collections import defaultdict
from functools import reduce
from operator import itemgetter
def max_aggregate(tuples_list):
    dict = defaultdict(int)
    for name, score in tuples_list:
        dict[name] += score
    return max(dict.items(), key=itemgetter(1))