def len_log(strings):
  longest = 0
  for string in strings:
    if len(string) > longest:
      longest = len(string)
  return longest