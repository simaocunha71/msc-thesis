
from itertools import chain
def combinations_list(nums: list) -> list:
    return list(chain(*[combinations(nums, r) for r in range(len(nums) + 1)]))


