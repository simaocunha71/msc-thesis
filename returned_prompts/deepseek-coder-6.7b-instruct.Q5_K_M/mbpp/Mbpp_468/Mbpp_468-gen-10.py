
def max_product(lst):
  lst.sort()
  return max(lst[0]*lst[1], lst[-1]*lst[-2])


