def len_log(lst: list) -> int:
  longest_word = max(lst, key=len)
  return len(longest_word)