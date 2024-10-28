def power_base_sum(base, power):
  result = base ** power
  return sum(map(int, str(result)))