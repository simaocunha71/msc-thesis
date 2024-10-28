def count_reverse_pairs(strings: list) -> int:
  pairs = 0
  for i in range(len(strings)):
    for j in range(i+1, len(strings)):
      if strings[i] == strings[j][::-1]:
        pairs += 1
  return pairs