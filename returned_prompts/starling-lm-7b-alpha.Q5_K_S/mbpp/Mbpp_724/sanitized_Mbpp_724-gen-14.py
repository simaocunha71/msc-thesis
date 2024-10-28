def power_base_sum(base: int,power: int):
  if power == 0:
    return 1
  return (base * power_base_sum(base,power-1))%10 + base