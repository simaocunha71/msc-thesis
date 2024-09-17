
from itertools import chain
def combinations_list(nums: list) -> list:
  return list(chain(*map(lambda x: [x], nums)))


