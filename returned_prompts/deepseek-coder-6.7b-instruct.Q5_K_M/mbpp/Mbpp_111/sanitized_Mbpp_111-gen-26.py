from itertools import chain
def common_in_nested_lists(list_of_lists):
  return set(chain(*list_of_lists)).intersection(*map(set, list_of_lists))