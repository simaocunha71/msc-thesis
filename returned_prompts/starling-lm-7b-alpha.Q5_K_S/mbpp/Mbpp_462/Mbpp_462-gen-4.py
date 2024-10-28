
def combinations_list(lst):
  result = [[]]
  for elem in lst:
    result += [x + [elem] for x in result]
  return result


