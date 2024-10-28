def find_remainder(arr: list, n: int) -> int:
  return (arr[0] % n) * (arr[-1] % n) % n