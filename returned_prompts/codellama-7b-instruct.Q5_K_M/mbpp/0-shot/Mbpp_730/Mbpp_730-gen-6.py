
import collections


def consecutive_duplicates(lst):
    return list(collections.OrderedDict.fromkeys(lst))
