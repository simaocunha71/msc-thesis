
def power_base_sum(base: int, power: int) -> int:
  total = 0
  for i in range(power+1):
    total += base ** i
  return total


