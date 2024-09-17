
def find_remainder(arr: list, n: int) -> int:
  product = 1
  for num in arr:
    product = (product * num) % n
  return product


