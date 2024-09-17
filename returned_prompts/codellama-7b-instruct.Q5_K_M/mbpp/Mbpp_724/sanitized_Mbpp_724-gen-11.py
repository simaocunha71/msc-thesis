def power_base_sum(base: int, power: int) -> int:
  sum = 0
  for digit in str(base**power):
    sum += int(digit)
  return sum