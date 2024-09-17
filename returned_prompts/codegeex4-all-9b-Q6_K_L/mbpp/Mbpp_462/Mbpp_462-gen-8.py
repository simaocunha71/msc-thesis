def combinations_list(nums: list) -> list:
  return list(itertools.chain(*[itertools.combinations(nums, i) for i in range(len(nums)+1)]))

