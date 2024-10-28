from itertools import combinations
def find_combinations(tuples):
  return list(combinations([i+j for i,j in tuples], 2))