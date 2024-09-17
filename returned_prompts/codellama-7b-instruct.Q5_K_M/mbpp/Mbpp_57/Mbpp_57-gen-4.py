
def find_Max_Num(digits: list) -> int:
  return int(''.join(sorted(map(str, digits), reverse=True)))


