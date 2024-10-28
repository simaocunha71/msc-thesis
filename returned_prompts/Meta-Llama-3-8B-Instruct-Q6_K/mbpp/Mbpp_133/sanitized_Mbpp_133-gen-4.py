def sum_negativenum(lst):
  return sum(x for x in lst if x < 0)  # or sum(-x for x in lst if x < 0) if you want to keep the sign