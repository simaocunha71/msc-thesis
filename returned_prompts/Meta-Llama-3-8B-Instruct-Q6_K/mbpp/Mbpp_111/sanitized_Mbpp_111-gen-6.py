from functools import reduce
from operator import or_
def common_in_nested_lists(nested_lists):
    return set(reduce(or_, (set(lst) for lst in nested_lists)))