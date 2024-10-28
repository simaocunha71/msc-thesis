
def count_Occurrence(tup, lst):
  count = 0
  for i in lst:
    count = count + tup.count(i)
  return count


