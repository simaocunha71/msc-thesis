
def zero_count(arr):
  zero_count = arr.count(0)
  non_zero_count = len([i for i in arr if i != 0])
  return zero_count / (zero_count + non_zero_count)


