
def division_elements(test_tup1, test_tup2):
  result = []
  for i in range(len(test_tup1)):
    result.append(test_tup1[i]/test_tup2[i])
  return tuple(result)


