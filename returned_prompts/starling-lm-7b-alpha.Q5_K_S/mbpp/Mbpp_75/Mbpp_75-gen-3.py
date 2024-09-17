
def find_tuples(test_tup, k):
  result = []
  for tup in test_tup:
    if all(i%k == 0 for i in tup):
      result.append(tup)
  return result


