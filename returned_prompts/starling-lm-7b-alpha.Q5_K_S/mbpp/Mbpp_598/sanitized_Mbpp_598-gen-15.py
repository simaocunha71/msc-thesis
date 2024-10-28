def armstrong_number(num: int):
  sum_of_cubes = sum(int(digit)**3 for digit in str(num))
  if num == sum_of_cubes:
    return True
  return False