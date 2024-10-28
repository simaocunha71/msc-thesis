import itertools
def combinations_list(nums):
    return list(itertools.chain.from_iterable(itertools.combinations(nums, r) for r in range(len(nums) + 1)))