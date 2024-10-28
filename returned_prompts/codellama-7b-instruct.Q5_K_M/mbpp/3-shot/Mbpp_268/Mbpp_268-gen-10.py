
def find_star_num(n):
  if n==1:
    return 1
  elif n==2:
    return 2
  else:
    return find_star_num(n-1)+find_star_num(n-2)


