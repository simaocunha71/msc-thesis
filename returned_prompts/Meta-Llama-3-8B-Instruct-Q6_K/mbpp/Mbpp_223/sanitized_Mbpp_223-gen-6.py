def is_majority(sorted_array, n, target):
  count = 0
  for num in sorted_array:
    if num == target:
      count += 1
  return count > n // 2