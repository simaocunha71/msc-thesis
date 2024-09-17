
def multiply_elements(test_tup):
  multiplied_tup = []
  for i in range(len(test_tup)-1):
    multiplied_tup.append(test_tup[i]*test_tup[i+1])
  return tuple(multiplied_tup)


