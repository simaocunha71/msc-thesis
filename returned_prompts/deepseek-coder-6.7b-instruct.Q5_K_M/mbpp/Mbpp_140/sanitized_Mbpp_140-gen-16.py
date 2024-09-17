def extract_singly(test_tup):
  result = []
  for i in test_tup:
    if isinstance(i, tuple):
      result += i
    else:
      result.append(i)
  return result