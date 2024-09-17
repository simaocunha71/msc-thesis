def count_reverse_pairs(strings: list) -> int:
  count = 0
  for i in range(len(strings)):
    for j in range(len(strings)):
      if strings[i] == strings[j][::-1]:
        count += 1
  return count