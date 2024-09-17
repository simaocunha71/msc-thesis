def power_base_sum(base, power):
  num = base ** power
  return sum(map(int, str(num)))