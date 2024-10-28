
def is_samepatterns(lst1, lst2):
  return len(set(zip(lst1, lst2))) == len(lst1) == len(lst2)


