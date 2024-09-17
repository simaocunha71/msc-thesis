def kth_element(nums: list, k: int) -> int:
  kth = sorted(nums)[k-1]
  return kth