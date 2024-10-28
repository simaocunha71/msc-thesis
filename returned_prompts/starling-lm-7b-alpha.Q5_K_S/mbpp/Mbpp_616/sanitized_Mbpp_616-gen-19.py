def tuple_modulo(test_tup1, test_tup2):
  modulo_tup = []
  for i in range(len(test_tup1)):
    modulo_tup.append((test_tup1[i] % test_tup2[i]))
  return tuple(modulo_tup)