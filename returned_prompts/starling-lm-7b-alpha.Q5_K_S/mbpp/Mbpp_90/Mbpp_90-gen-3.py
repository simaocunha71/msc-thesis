
def len_log(words: list) -> int:
  max_len = 0
  for word in words:
    if len(word) > max_len:
      max_len = len(word)
  return max_len


