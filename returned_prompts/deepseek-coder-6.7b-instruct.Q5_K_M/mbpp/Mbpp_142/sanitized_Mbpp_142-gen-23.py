def count_samepair(l1, l2, l3):
  return sum(1 for a, b, c in zip(l1, l2, l3) if a == b == c)