
def check_occurences(test_tup):
  result = {}
  for i in test_tup:
    if i in result:
      result[i] += 1
    else:
      result[i] = 1
  return result


