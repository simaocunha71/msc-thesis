def check_min_heap(lst: list) -> bool:
  n = len(lst)
  for i in range(n):
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and lst[i] > lst[left]:
      return False
    if right < n and lst[i] > lst[right]:
      return False
  return True