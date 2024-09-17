def pancake_sort(lst: list) -> list:
  for i in range(len(lst)-1, 0, -1):
    max_index = lst.index(max(lst[:i+1]))
    if max_index != i:
      lst[max_index:i+1] = reversed(lst[max_index:i+1])
      lst[:i+1] = reversed(lst[:i+1])
  return lst