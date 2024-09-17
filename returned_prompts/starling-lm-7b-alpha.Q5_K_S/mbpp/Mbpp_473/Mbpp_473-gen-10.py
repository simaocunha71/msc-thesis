
def tuple_intersection(tups1, tups2):
  set1 = set(tups1)
  set2 = set(tups2)
  intersection = set1 & set2
  return [(x, y) for x, y in intersection]


