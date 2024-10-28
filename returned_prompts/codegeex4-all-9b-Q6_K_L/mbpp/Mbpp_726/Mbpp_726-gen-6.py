def multiply_elements(test_tuple):
  res = []
  for i in range(len(test_tuple)-1):
    res.append(test_tuple[i]*test_tuple[i+1])
  return tuple(res)

