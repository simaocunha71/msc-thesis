
def power_base_sum(base: int, power: int) -> int:
  return sum([int(str(base ** i)) for i in range(power+1)])


