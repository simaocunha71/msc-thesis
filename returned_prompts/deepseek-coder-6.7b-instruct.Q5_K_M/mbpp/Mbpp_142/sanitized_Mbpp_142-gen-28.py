def count_samepair(lst1, lst2, lst3):
  return sum(1 for a, b, c in zip(lst1, lst2, lst3) if a == b == c)