
def combinations_list(nums: list) -> list:
  return [[]] + [list(i) for i in itertools.chain.from_iterable(itertools.combinations(nums, r) for r in range(len(nums)+1))


