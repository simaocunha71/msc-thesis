def power_base_sum(base, power):
  total_sum = 0
  base_power = base ** power
  while base_power > 0:
    total_sum += base_power % 10
    base_power //= 10
  return total_sum

