def max_Product(arr):
  arr.sort()
  return (arr[-1]*arr[-2],arr[-2]*arr[-3])