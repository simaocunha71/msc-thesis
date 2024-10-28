
def count_first_elements(test_tup):
  counter = 0
  for num in test_tup:
    if isinstance(num, tuple):
      break
    else:
      counter += 1
  return counter


