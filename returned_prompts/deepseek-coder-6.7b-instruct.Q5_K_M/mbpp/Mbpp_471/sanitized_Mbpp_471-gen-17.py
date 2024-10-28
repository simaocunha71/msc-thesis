def find_remainder(arr: list,n: int) -> int:
  prod = 1
  for num in arr:
    prod *= num
  return prod % n