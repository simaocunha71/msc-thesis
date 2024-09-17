def power_base_sum(base: int, power: int):
  if power == 0:
    return 1
  elif power == 1:
    return base
  else:
    return base + power_base_sum(base, power - 1)