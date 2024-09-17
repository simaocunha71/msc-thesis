def find_star_num(n):
  star_num = 0
  for i in range(1, n+1):
    star_num += 3 * (i-1) + 1
  return star_num