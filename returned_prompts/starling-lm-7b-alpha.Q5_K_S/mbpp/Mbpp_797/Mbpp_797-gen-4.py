
def sum_in_range(l, r):
  if l % 2 == 0:
    l += 1
  return sum(range(l, r + 1, 2))


