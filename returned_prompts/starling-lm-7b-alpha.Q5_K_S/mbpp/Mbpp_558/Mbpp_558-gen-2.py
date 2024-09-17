
def digit_distance_nums(num1: int, num2: int) -> int:
  return sum(abs(int(c1) - int(c2)) for c1, c2 in zip(str(num1), str(num2)))


