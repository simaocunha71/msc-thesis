from collections import Counter
from collections import OrderedDict
def count_Occurrence(tup, lst):
    count_dict = {}
    for i in lst:
        count_dict[i] = tup.count(i)
    return sum(count_dict.values())