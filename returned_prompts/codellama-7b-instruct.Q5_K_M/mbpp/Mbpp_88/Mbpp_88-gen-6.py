
def freq_count(lst):
  result = {}
  for i in lst:
    if i in result:
      result[i] += 1
    else:
      result[i] = 1
  return result


