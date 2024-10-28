
from typing import List
def common_in_nested_lists(nested_lists: List[List[int]]) -> set:
  return set(nested_lists[0]).intersection(*map(set, nested_lists))


