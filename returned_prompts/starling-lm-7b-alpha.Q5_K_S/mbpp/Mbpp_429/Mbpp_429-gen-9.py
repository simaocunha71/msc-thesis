
def and_tuples(test_tup1, test_tup2):
  and_elems = []
  for i in range(len(test_tup1)):
    and_elems.append(test_tup1[i] & test_tup2[i])
  return tuple(and_elems)


