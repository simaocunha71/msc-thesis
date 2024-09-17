
def power_base_sum(base: int, power: int) -> int:
  sum = 0
  for i in range(power + 1):
    sum += pow(base, i, 10)
  return sum


