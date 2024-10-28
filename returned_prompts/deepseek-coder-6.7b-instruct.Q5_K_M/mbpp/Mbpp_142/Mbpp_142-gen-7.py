
def count_samepair(l1, l2, l3):
  return sum(a == b == c for a, b, c in zip(l1, l2, l3))


