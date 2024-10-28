import itertools
def combinations_list(nums: list) -> list:
  return list(itertools.chain.from_iterable(itertools.combinations(nums, i) for i in range(1, len(nums)+1)))