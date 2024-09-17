
def len_log(words: list) -> int:
  longest_word = ""
  for word in words:
    if len(word) > len(longest_word):
      longest_word = word
  return len(longest_word)


