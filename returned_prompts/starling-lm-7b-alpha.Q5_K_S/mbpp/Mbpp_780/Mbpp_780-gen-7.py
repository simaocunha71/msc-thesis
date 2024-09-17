
def find_combinations(test_tup1):
  combinations = []
  for i in test_tup1:
    for j in test_tup1:
      if i != j:
        combinations.append((i[0] + j[0], i[1] + j[1]))
  return combinations


