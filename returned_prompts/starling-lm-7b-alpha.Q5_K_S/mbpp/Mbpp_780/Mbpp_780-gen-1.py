
def find_combinations(test_tup):
  result = []
  for i in test_tup:
    for j in test_tup:
      result.append(tuple(map(sum, zip(i, j))))
  return result


