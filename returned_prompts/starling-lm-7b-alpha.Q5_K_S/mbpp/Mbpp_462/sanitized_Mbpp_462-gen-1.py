from itertools import chain
from itertools import chain
def combinations_list(lst):
    return list(chain(*map(lambda x: [x] + combinations_list(lst[:i] + lst[i+1:]) for i, x in enumerate(lst))))