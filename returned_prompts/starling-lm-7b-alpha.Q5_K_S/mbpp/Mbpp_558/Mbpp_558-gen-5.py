
def digit_distance_nums(n: int,m: int) -> int:
  return sum(abs(int(str(n)[i]) - int(str(m)[i])) for i in range(len(str(n))))


