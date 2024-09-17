
def find_star_num(n):
  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return find_star_num(n-1) + find_star_num(n-2)


