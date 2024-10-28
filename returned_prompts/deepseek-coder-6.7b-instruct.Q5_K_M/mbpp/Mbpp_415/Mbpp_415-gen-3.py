
def max_Product(lst):
  lst.sort()
  if lst[0]*lst[1] > lst[-1]*lst[-2]:
    return (lst[0], lst[1])
  else:
    return (lst[-1], lst[-2])


