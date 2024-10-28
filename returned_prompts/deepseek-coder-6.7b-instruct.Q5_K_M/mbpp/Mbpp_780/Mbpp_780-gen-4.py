
from itertools import combinations
def find_combinations(nums):
  return list(combinations([i+j for i, j in nums], 2))


