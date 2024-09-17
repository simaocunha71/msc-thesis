def digit_distance_nums(n1, n2):
  return sum(abs(int(d1)-int(d2)) for d1, d2 in zip(str(n1), str(n2)))