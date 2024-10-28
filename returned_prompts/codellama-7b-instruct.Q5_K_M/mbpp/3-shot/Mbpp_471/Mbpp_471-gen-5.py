
def find_remainder(arr: list,modulo: int) -> int:
  result = 1
  for i in arr:
    result *= i
    result %= modulo
  return result


