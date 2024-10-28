
def len_log(words: list) -> int:
  longest_word_len = 0
  for word in words:
    if len(word) > longest_word_len:
      longest_word_len = len(word)
  return longest_word_len


