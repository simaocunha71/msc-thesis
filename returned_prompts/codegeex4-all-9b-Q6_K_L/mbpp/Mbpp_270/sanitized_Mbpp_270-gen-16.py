def sum_even_and_even_index(lst: list) -> int:
  total = 0
  for i in range(0, len(lst), 2):
    if lst[i] % 2 == 0:
      total += lst[i]
  return total