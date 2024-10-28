
def power_base_sum(base: int, power: int):
  sum_of_digits = 0
  for _ in range(power):
    sum_of_digits += base % 10
    base = base // 10
  return sum_of_digits


