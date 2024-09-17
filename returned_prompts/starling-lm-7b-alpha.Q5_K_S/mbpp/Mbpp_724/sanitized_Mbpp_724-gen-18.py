def power_base_sum(base, power):
  sum_base = 0
  for i in range(power+1):
    sum_base += base**i
  return sum_base