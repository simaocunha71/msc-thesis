def sum_in_range(l, r):
  return sum(i for i in range(l,r+1) if i % 2 != 0)  # or sum(range(l+1,r+1,2)) if you want a more pythonic way