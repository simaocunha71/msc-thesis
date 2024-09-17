def multiply_elements(test_tup):
  new_tup = []
  for i in range(len(test_tup)-1):
    new_tup.append(test_tup[i]*test_tup[i+1])
  return tuple(new_tup)