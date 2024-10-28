
def count_reverse_pairs(strings: list) -> int:
  count = 0
  for string in strings:
    if string == string[::-1]:
      count += 1
  return count


