
def count_reverse_pairs(strings: list) -> int:
  count = 0
  for i in range(len(strings)):
    for j in range(len(strings)):
      if strings[i][::-1] == strings[j]:
        count += 1
  return count


