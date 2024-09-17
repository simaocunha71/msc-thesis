
def find_remainder(arr: list, n: int) -> int:
  product = 1
  for i in arr:
    product = (product * i) % n
  return product


