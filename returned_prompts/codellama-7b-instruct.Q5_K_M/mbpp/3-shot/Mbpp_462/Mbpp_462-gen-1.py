
def combinations_list(lst):
  return [list(i) for i in set(map(tuple,combinations_with_replacement(lst,r=len(lst))))]


