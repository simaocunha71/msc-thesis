def count_first_elements(test_tuple):
  counter = 0
  for i in test_tuple:
    if type(i) != tuple:
      counter += 1
    else:
      break
  return counter