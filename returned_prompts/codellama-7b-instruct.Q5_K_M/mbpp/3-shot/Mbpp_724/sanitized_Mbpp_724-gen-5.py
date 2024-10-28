def power_base_sum(base,power):
  num = base**power
  sum = 0
  while num > 0:
    sum += num%10
    num //= 10
  return sum