def find_kth(a: list, b: list, k: int) -> int:
  if k > len(a)+len(b):
    return "Index out of range"
  if k <= len(a):
    return a[k-1]
  if k <= len(b):
    return b[k-1]
  if a[-1] < b[-1]:
    return b[k-len(a)-1]
  return a[k-len(b)-1]