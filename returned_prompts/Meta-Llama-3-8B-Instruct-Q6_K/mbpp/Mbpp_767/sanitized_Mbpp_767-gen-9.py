def get_pairs_count(lst, sum):
  lst.sort()
  left, right = 0, len(lst) - 1
  count = 0
  while left <= right:
    if lst[left] + lst[right] == sum:
      count += 1
      left += 1
      right -= 1
    elif lst[left] + lst[right] < sum:
      left += 1
    else:
      right -= 1
  return count * 2 if sum % 2 == 0 else count * 2 + 1