
def index_multiplication(test_tup1, test_tup2):
  multiplied_tup = []
  for i in range(len(test_tup1)):
    multiplied_tup.append((test_tup1[i] * test_tup2[i]))
  return tuple(multiplied_tup)


