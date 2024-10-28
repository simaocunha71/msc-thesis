def power_base_sum(base: int, power: int) -> int:
  return sum(int(digit) for digit in str(base**power))